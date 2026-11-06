# LinkedIn news feed and Zapier Free

Status: the feed and automatic preparation are configured for GitHub Pages. No Zap or LinkedIn connection has been created. Automatic LinkedIn publication must remain OFF until the live acceptance checks below pass.

## Feed and editorial workflow

After approved deployment, the RSS 2.0 endpoint will be:
`https://www.africaeuropecoremath.org/linkedin.xml`

`linkedin.xml` uses normal GitHub Pages Liquid, not a custom plugin. It emits title, HTML-stripped summary (the existing news-card excerpt helper, with normal RSS description entity encoding), canonical URL, RFC 822 publication date, and a UUID GUID with `isPermaLink="false"`. Compatible images use Media RSS; local images also have an RSS enclosure with actual byte length. No item limit is imposed, so a short outage does not immediately remove older eligible items.

All 53 articles present at implementation have a UUID in `linkedin_id`; `_data/linkedin_history.json` permanently excludes those IDs. Historical exclusions survive renames and date changes. Do not regenerate the baseline or change an existing ID. Newly added articles are eligible by default once prepared, including backdated articles. Jekyll still controls publication: drafts, `published: false`, and future posts are not emitted by a normal production build.

Authors continue to create/edit `_posts` Markdown files, commit, and push/merge to `main`. **No preparation command is required.** Prefer an existing `card_excerpt` for the short description. Set the YAML boolean `linkedin: false` to opt out; this cannot retract an already published/queued LinkedIn post.

`.github/workflows/prepare-linkedin-news.yml` runs after relevant pushes to `main`. It checks out the latest main, runs preparation and validation, commits only article metadata/image-manifest/derivative changes when needed, and explicitly requests a Pages rebuild. It uses the repository's existing `GITHUB_TOKEN`, not a new account, service or personal token. Pillow is the same conversion dependency already used by preparation, pinned to the locally verified version. The existing PR/asset check validates preparation in a disposable checkout without committing or requesting deployment.

`linkedin_id` is necessary because a date, title, filename or URL cannot provide rename-safe identity. Preserve it when moving/renaming an article. When copying an article to create a genuinely new one, remove the copied ID; automation assigns a new one. Duplicate IDs fail validation. Do not change an existing ID, including on excluded articles.

The preparation job is serialized. If an editor or the opportunities importer advances main, a rejected push is retried against the latest source without force-pushing or overwriting that update. A failed attempt's UUID is never published. Successful UUIDs are stored in Git; subsequent preparation is a no-op unless input changes. Bot commits do not trigger another Actions run/Pages build, so the job validates its own result and explicitly requests the rebuild, even on a no-op rerun. It retries build requests when Pages is busy.

**Publication timing:** branch-based GitHub Pages may build the author's original commit before preparation finishes. The article can therefore appear on the website first, but is omitted from the LinkedIn feed until a permanent ID is committed and rebuilt. Strictly preventing any website publication before preparation would require switching the entire Pages deployment to a gated Actions pipeline; that change is intentionally not made. No LinkedIn publication is possible from an ID-less feed item. This keeps the existing website deployment and daily rebuild workflow intact.

Before deploying this workflow, confirm repository rules permit the Actions bot to commit preparation to `main` and request Pages builds (the existing opportunities importer and daily refresh use these respective permission patterns). Do not bypass branch protection. If writes are prohibited, leave automation off and either allow this narrowly scoped workflow under repository policy or use a separately approved deployment-pipeline change. Check the first real run after deployment. A failed run needs attention/rerun, not routine author preparation. The workflow's manual dispatch is for recovery only.

For optional local previews, the existing `ruby scripts/prepare_linkedin.rb --prepare` command remains available; without `--prepare`, it validates without writing. `scripts/commit_linkedin_preparation.sh` is restricted to a clean, disposable Actions checkout and must not be run in an editor's working directory.

## Optional images

The preparation script uses the existing `image` field. Inspect its suitability and social-use permission as part of editorial review. It never substitutes a logo. For the rare exception, `linkedin_image: false` suppresses an unsuitable article image, or `linkedin_image: /assets/...` selects a suitable alternate. No extra description field is needed.

Local JPG/PNG/GIF files are checked by signature. Local AVIF files are converted into separate PNGs under `assets/images/linkedin/`, named by the source's SHA-256 digest. Originals are not modified or resized. Conversion uses Python 3 with Pillow 11.3 or newer (AVIF support). Install it in an authoring virtual environment with `python3 -m venv ../linkedin-image-venv`, activate that environment, then `python3 -m pip install 'Pillow>=11.3,<13'`. Keep the environment outside the website source. Actions installs this existing dependency automatically. Local authors only need it for optional AVIF previews; GitHub Pages itself does not need it. If conversion fails, correct it before publishing or explicitly suppress the image. Visually review any new derivative before committing.

HTTPS JPG/PNG/GIF URLs can be emitted without downloading them; their availability, actual format, size and permissions require editorial checking. Unsupported formats (including remote AVIF) are omitted. To use one, supply a reviewed local compatible derivative via `linkedin_image`. Image absence does not exclude the article: it remains a text-and-link item. LinkedIn may independently generate a link preview; the feed does not force a fallback image.

## Configure one two-step Zap — only after deployment approval

1. **RSS trigger:** select RSS by Zapier → New Item in Feed, using the endpoint above. Choose **Different Guid/URL**, never Different Content or Anything is Different. Inspect the trigger sample to confirm the UUID GUID is exposed. The initial production feed is intentionally empty; do not remove historical exclusions to obtain a sample. Arrange an explicitly authorised new pilot article when ready. Test/sample selection does not constitute permission to publish a LinkedIn action.
2. **LinkedIn action:** connect an authorised CoRE-Math Page administrator, choose LinkedIn → Create Company Update, and select the organisation page `https://www.linkedin.com/company/core-math/`. Do not select the LinkedIn group or a personal profile.
3. **Map fields:** put RSS Title, Description and Link in Update Content, separated by newlines. Map Link to Media URL and Title/Description to Preview Title/Description where applicable. Map the enclosure URL (or Media RSS content URL exposed by the trigger) to Image, using the connector's URL image input. Confirm the actual trigger output labels; they can vary. Leave image data empty for articles without an image. Do not hard-code a sample image. Verify that the SAME action configuration accepts both populated and empty image data; do not assume the connector automatically changes image mode. If it requires branching, this design cannot meet optional-image behaviour in one Free Zap: leave it off and review the configuration rather than adding a paid step or silently dropping images.
4. **Mandatory mentions:** enable **Allow Mentions in content?**. Add two fixed, resolved organisation mentions to Update Content using the current action's mention instructions/selector. Targets:
   - African Research Universities Alliance (ARUA): https://www.linkedin.com/company/african-research-universities-alliance-arua/
   - The Guild of European Research-Intensive Universities: https://www.linkedin.com/company/the-guild-eu/

   These URLs identify the targets; pasting them or plain `@` names is NOT a valid mention configuration. If the action requires entity IDs/URNs, resolve them through its supported mechanism and use the exact official names. No numeric IDs have been guessed or embedded in the feed. LinkedIn's structured mention format is `@[Exact organisation name](urn:li:organization:ID)`, but use it only if the Zapier action explicitly supports that input; it is not a verified Zapier recipe. If the editor cannot resolve both entities, stop and consult Zapier support. The feed deliberately contains article content, not misleading plain-text tags.
5. **Authorised live acceptance test:** keep automatic operation off. Testing the LinkedIn action publishes a real post and needs explicit permission. Test both an image item and a no-image item. Inspect the resulting posts on LinkedIn, click both partner names, and verify they open the exact official pages. Check the image, title, description and article link, including correct rendering of ampersands/quotes in RSS description entities. Also verify a repeated poll and a changed title/date/URL with the same GUID do not create another post; Zapier's public wording says “Guid/URL”, so UUID precedence under URL changes must be verified, not assumed. Never deliberately replay the publishing action to test trigger deduplication. Record test article GUIDs, resulting LinkedIn post URLs and outcomes in the editorial log.
6. **Activate only after all checks pass:** confirm that the Zap contains only one RSS trigger and one LinkedIn action and runs on Free after any trial ends. Reconcile pilot items already posted before enabling it: exclude pilot articles with `linkedin: false` and retain their GUIDs/log entries so testing cannot cause a second live post. Do not turn it on if either mention is plain text, optional images fail, or URL changes bypass GUID deduplication. No automatic activation is part of this repository.

## Free-plan limits and recovery

Zapier Free currently allows 100 tasks/month, one trigger plus one action, and 15-minute polling. At 20–30 articles annually, task volume is small. Filters, extra lookup/logging steps and automatic replay are not part of this two-step design. Feed-side eligibility replaces a Zapier filter.

Stable GUIDs prevent identity changes on edits/rebuilds. They do not guarantee exactly-once delivery by an external service. Zapier deduplication is per Zap; recreating/duplicating a Zap or manually replaying an action can create duplicates. There is no transactional publication ledger in this implementation. Keep a small manual record of GUID → LinkedIn post URL, especially for pilots and recovery. Never change an ID to force a retry.

On an error, pause and inspect LinkedIn before retrying. A timeout may mean the post succeeded but the response was lost. If present, record it and do not retry; if uncertain, investigate manually. Reconnect expired authorisation when required. Before replacing a Zap, reconcile published items and exclude those items from the feed. Exclusions are not a way to recall items already fetched by Zapier. Partner renames or connector changes require re-verification; the repository cannot enforce rendering of tags inside LinkedIn. If this operational limitation becomes unacceptable, revisit a durable publication log separately.

## Local verification (optional for authors)

Run from the repository root with the existing Jekyll/GitHub Pages environment:

```sh
ruby scripts/prepare_linkedin.rb --prepare
ruby scripts/prepare_linkedin.rb
python3 scripts/check_local_assets.py
JEKYLL_BIN="$(command -v jekyll)" python3 -m unittest discover -s tests -v
jekyll build
```

`tests/test_linkedin_feed.py` uses disposable copies, actual Jekyll builds and XML parsing. It checks historical exclusion, new backdated posts, opt-out, image/no-image cases, AVIF derivatives, unchanged originals, XML escaping, GUID stability across rebuilds/renames/date changes and duplicate-ID rejection. It needs Python with Pillow 11.3 or newer for the AVIF fixture. Without `JEKYLL_BIN`, that integration test is explicitly skipped; the existing Python tests still run. `tests/test_linkedin_preparation_workflow.py` also executes the actual commit script against disposable local Git repositories, checking persistent IDs, concurrent editor pushes, idempotent reruns and renamed articles. Live Zapier parsing and LinkedIn rendering remain manual acceptance checks.

## Vendor references (checked 6 November 2026)

- [Zapier Free plan](https://help.zapier.com/hc/en-us/articles/32337438839565-What-s-included-in-Zapier-s-Free-plan)
- [RSS trigger and GUID/URL behaviour](https://help.zapier.com/hc/en-us/articles/8496279482125-Trigger-Zap-workflows-from-new-RSS-feed-items)
- [LinkedIn action fields](https://zapier.com/apps/linkedin/integrations)
- [LinkedIn action capabilities and Page administration](https://help.zapier.com/hc/en-us/articles/8495987891853-How-to-get-started-with-LinkedIn-on-Zapier)
- [Zapier duplicate handling](https://help.zapier.com/hc/en-us/articles/8496260269965-How-Zapier-handles-duplicate-data-in-Zap-workflows)
- [LinkedIn Posts API and mention requirements](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)

- [GitHub Pages: bot commits need an explicit build request](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
