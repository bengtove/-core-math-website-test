"""Integration test: JEKYLL_BIN=/path/to/jekyll python3 -m unittest discover -s tests.
Uses isolated copies; never creates a publishable fixture in the real repository.
"""
import hashlib
import html
import json
import os
import re
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class LinkedInFeedTest(unittest.TestCase):
    @unittest.skipUnless(os.environ.get('JEKYLL_BIN'), 'Set JEKYLL_BIN to run real Jekyll integration checks')
    def test_feed_lifecycle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'source'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '_site', '__pycache__', '.sass-cache'))
            out = Path(tmp) / 'output'
            def prepare(check=False, success=True):
                args = ['ruby', 'scripts/prepare_linkedin.rb'] + ([] if check else ['--prepare'])
                result = subprocess.run(args, cwd=root, capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)
            def build():
                result = subprocess.run(['ruby', os.environ['JEKYLL_BIN'], 'build', '--source', str(root), '--destination', str(out)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                rss = ET.parse(out / 'linkedin.xml').getroot()
                self.assertEqual(rss.attrib['version'], '2.0')
                self.assertIsNotNone(rss.find('channel/{http://www.w3.org/2005/Atom}link'))
                return rss.findall('channel/item')
            prepare(check=True)
            self.assertEqual(build(), [])
            history = json.loads((root / '_data/linkedin_history.json').read_text())
            self.assertEqual(len(history), 53)
            # Dates, URLs and titles of historical articles may change without backfill.
            old = sorted((root / '_posts').glob('*.md'))[0]
            old.write_text(re.sub(r'(?m)^date:.*$', 'date: 2020-01-01', old.read_text()).replace('\n---\n', '\npermalink: /historical-renamed/\n---\n', 1))
            old.rename(root / '_posts/2020-01-01-historical-renamed.md')
            self.assertEqual(build(), [])
            fixtures = {
                'plain': '',
                'image': 'image: /assets/images/news/cnrs-logo.png\n',
                'avif': 'image: /assets/images/news/560c14_574ae92fac3f4e6da79ed0326d46f997~mv2.jpeg.avif\n',
                'excluded': 'linkedin: false\n',
                'unpublished': 'published: false\n',
                'future': 'date: 2099-01-01\n',
                'suppressed-image': 'image: /assets/images/news/cnrs-logo.png\nlinkedin_image: false\n',
            }
            for name, fields in fixtures.items():
                (root / '_posts' / ('2020-01-01-fixture-' + name + '.md')).write_text('---\ntitle: "Fixture & <' + name + '>"\ncard_excerpt: "A short & clear description."\n' + fields + '---\n\nBody.\n')
            # New backdated articles are eligible; date cutoffs are not used.
            prepare(check=True, success=False)
            original = root / 'assets/images/news/560c14_574ae92fac3f4e6da79ed0326d46f997~mv2.jpeg.avif'
            digest = hashlib.sha256(original.read_bytes()).hexdigest()
            prepare()
            prepare(check=True)
            items = build()
            self.assertEqual(len(items), 4)
            by_title = {i.findtext('title'): i for i in items}
            for name in ['plain', 'suppressed-image']:
                self.assertIsNone(by_title['Fixture & <' + name + '>'].find('enclosure'))
                self.assertIsNone(by_title['Fixture & <' + name + '>'].find('{http://search.yahoo.com/mrss/}content'))
            for name in ['image', 'avif']:
                item = by_title['Fixture & <' + name + '>']
                enc = item.find('enclosure')
                self.assertEqual(enc.attrib['type'], 'image/png')
                self.assertGreater(int(enc.attrib['length']), 0)
                self.assertTrue(enc.attrib['url'].startswith('https://www.africaeuropecoremath.org/assets/'))
            self.assertEqual(hashlib.sha256(original.read_bytes()).hexdigest(), digest)
            from PIL import Image
            derivative = root / 'assets/images/linkedin' / (digest + '.png')
            with Image.open(original) as a, Image.open(derivative) as b:
                self.assertEqual(a.size, b.size)
                self.assertEqual(b.format, 'PNG')
            for item in items:
                # RSS descriptions allow HTML entities after XML decoding.
                self.assertEqual(html.unescape(item.findtext('description')), 'A short & clear description.')
                self.assertTrue(item.findtext('link').startswith('https://www.africaeuropecoremath.org/news/'))
                self.assertIsNotNone(item.findtext('pubDate'))
                self.assertEqual(item.find('guid').attrib['isPermaLink'], 'false')
            ids = {i.findtext('guid') for i in items}
            self.assertEqual(len(ids), 4)
            self.assertEqual(ids, {i.findtext('guid') for i in build()})
            plain = root / '_posts/2020-01-01-fixture-plain.md'
            text = plain.read_text().replace('2020-01-01', '2021-02-02').replace('Fixture & <plain>', 'Renamed title')
            renamed = root / '_posts/2021-02-02-completely-renamed.md'
            plain.rename(renamed)
            renamed.write_text(text)
            prepare()
            updated = build()
            self.assertEqual(ids, {i.findtext('guid') for i in updated})
            self.assertTrue(next(i for i in updated if i.findtext('title') == 'Renamed title').findtext('link').endswith('/news/2021/completely-renamed/'))
            # Re-running preparation must not modify identities or image manifest.
            before = renamed.read_bytes()
            prepare()
            self.assertEqual(before, renamed.read_bytes())
            # Copies must receive a new UUID, not silently reuse an existing identity.
            (root / '_posts/2021-02-03-copy.md').write_text(renamed.read_text())
            prepare(check=True, success=False)
