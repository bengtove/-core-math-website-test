#!/usr/bin/env bash
# Only run in a disposable Actions checkout; never in an editor's working tree.
set -euo pipefail
if [[ "${GITHUB_ACTIONS:-}" != "true" ]]; then
  echo 'This command is for a disposable GitHub Actions checkout only.' >&2
  exit 1
fi
if [[ -n "$(git status --porcelain)" ]]; then
  echo 'Preparation requires a clean checkout.' >&2
  exit 1
fi
git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
for attempt in 1 2 3 4 5; do
  # Another editor or the opportunities importer may advance main during a run.
  # Failed pushes are never forced; regenerate against the latest source instead.
  git fetch origin main
  git reset --hard origin/main
  ruby scripts/prepare_linkedin.rb --prepare
  ruby scripts/prepare_linkedin.rb
  python3 scripts/check_local_assets.py
  git add -- _posts _data/linkedin_images.json
  if [[ -d assets/images/linkedin ]]; then
    git add -- assets/images/linkedin
  fi
  if git diff --cached --quiet; then
    echo 'LinkedIn preparation is already up to date.'
    exit 0
  fi
  git diff --cached --check
  git commit -m 'Prepare permanent LinkedIn news metadata'
  if git push origin HEAD:main; then
    exit 0
  fi
  echo "Main advanced or push was rejected (attempt $attempt); retrying without force." >&2
  sleep 2
done
echo 'Cannot persist preparation. Check branch permissions/protection and rerun.' >&2
exit 1
