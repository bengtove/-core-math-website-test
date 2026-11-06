"""Exercise the real preparation/commit script using local, disposable Git repos."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class AutomaticPreparationTest(unittest.TestCase):
    def test_persists_ids_retries_concurrent_push_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            remote, seed, runner, rival = [tmp / p for p in ['remote.git', 'seed', 'runner', 'rival']]
            real_git = shutil.which('git')
            def git(*args, cwd=seed):
                return subprocess.check_output([real_git, *args], cwd=cwd, stderr=subprocess.STDOUT, text=True).strip()
            shutil.copytree(ROOT, seed, ignore=shutil.ignore_patterns('.git', '_site', '__pycache__', '.sass-cache'))
            git('init', '--bare', str(remote), cwd=tmp)
            git('init', '-b', 'main')
            git('config', 'user.name', 'Test editor')
            git('config', 'user.email', 'editor@example.invalid')
            git('add', '.')
            git('commit', '-m', 'Existing website and historical exclusions')
            article = '_posts/2020-01-01-new-automatic-test.md'
            (seed / article).write_text('---\ntitle: Automatic preparation\n---\n\nA new backdated article.\n')
            git('add', article)
            git('commit', '-m', 'Publish a news article without manual preparation')
            git('remote', 'add', 'origin', str(remote))
            git('push', '-u', 'origin', 'main')
            git('clone', '-b', 'main', str(remote), str(runner), cwd=tmp)
            git('clone', '-b', 'main', str(remote), str(rival), cwd=tmp)
            git('config', 'user.name', 'Concurrent editor', cwd=rival)
            git('config', 'user.email', 'concurrent@example.invalid', cwd=rival)
            # Insert a real competing main update immediately before the first push.
            wrapper = tmp / 'bin'; wrapper.mkdir()
            (wrapper / 'git').write_text('''#!/usr/bin/env bash
set -e
if [[ "$1" == push && ! -e "$RACE_MARKER" ]]; then
  touch "$RACE_MARKER"
  echo 'Concurrent editorial update' > "$RIVAL/concurrent.txt"
  "$REAL_GIT" -C "$RIVAL" add concurrent.txt
  "$REAL_GIT" -C "$RIVAL" commit -m 'Concurrent editorial update' >&2
  "$REAL_GIT" -C "$RIVAL" push origin HEAD:main >&2
fi
exec "$REAL_GIT" "$@"
''')
            (wrapper / 'git').chmod(0o755)
            env = dict(os.environ, GITHUB_ACTIONS='true', PATH=str(wrapper) + os.pathsep + os.environ['PATH'], REAL_GIT=real_git, RIVAL=str(rival), RACE_MARKER=str(tmp / 'raced'))
            def prepare():
                result = subprocess.run(['bash', 'scripts/commit_linkedin_preparation.sh'], cwd=runner, env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                return result.stdout + result.stderr
            log = prepare()
            self.assertIn('retrying without force', log)
            self.assertEqual((runner / 'concurrent.txt').read_text(), 'Concurrent editorial update\n')
            prepared = (runner / article).read_text()
            self.assertIn('linkedin_id: ', prepared)
            self.assertEqual(git('status', '--porcelain', cwd=runner), '')
            self.assertEqual(git('rev-parse', 'HEAD', cwd=runner), git('rev-parse', 'refs/heads/main', cwd=remote))
            head = git('rev-parse', 'HEAD', cwd=runner)
            prepare()
            self.assertEqual(git('rev-parse', 'HEAD', cwd=runner), head)
            self.assertEqual((runner / article).read_text(), prepared)
            # A normal rename/date/title edit keeps the saved UUID and makes no bot commit.
            renamed = '_posts/2021-02-02-renamed-automatic-test.md'
            git('mv', article, renamed, cwd=runner)
            (runner / renamed).write_text(prepared.replace('title: Automatic preparation', 'title: Edited title\ndate: 2021-02-02'))
            git('add', renamed, cwd=runner)
            git('commit', '-m', 'Rename and edit article', cwd=runner)
            git('push', 'origin', 'HEAD:main', cwd=runner)
            edited_head = git('rev-parse', 'HEAD', cwd=runner)
            prepare()
            self.assertEqual(git('rev-parse', 'HEAD', cwd=runner), edited_head)
            self.assertEqual((runner / renamed).read_text().splitlines()[1], prepared.splitlines()[1])
            self.assertEqual(git('show', 'HEAD:_data/linkedin_history.json', cwd=runner), (ROOT / '_data/linkedin_history.json').read_text().strip())

    def test_refuses_an_editors_working_tree(self):
        env = dict(os.environ, GITHUB_ACTIONS='false')
        result = subprocess.run(['bash', 'scripts/commit_linkedin_preparation.sh'], cwd=ROOT, env=env, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('disposable GitHub Actions checkout', result.stderr)
