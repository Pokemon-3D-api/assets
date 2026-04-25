#!/bin/bash
set -e

COMMIT_MESSAGE="chore: asset sync & optimization 🐉✨"
MAX_COMMITS=5
REMOTE_REPO="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

git config --global user.name  "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"

echo "🧹 Cleaning temporary raw files..."
rm -rf models/glb/* || true

echo "📊 Updating README stats..."
python scripts/update_stats.py
STATS_EXIT=$?
if [ "$STATS_EXIT" -ne 0 ] && [ "$STATS_EXIT" -ne 2 ]; then
  echo "❌ update_stats.py failed with exit code $STATS_EXIT"
  exit 1
fi

git add -A

if [ -z "$(git status --porcelain)" ]; then
  echo "✨ No changes to commit. Everything is up to date."
  exit 0
fi

echo "🔍 Changes detected:"
git status --short

COUNT=$(git rev-list --count HEAD)
echo "📊 Current commit count: $COUNT"

if [ "$COUNT" -gt "$MAX_COMMITS" ]; then
  echo "📉 Limit reached ($MAX_COMMITS). Squashing history..."

  git checkout --orphan temp_branch
  git add -A
  git commit -m "chore: fresh start (assets synced) 💎"

  git branch -D main
  git branch -m main

  git push "$REMOTE_REPO" main --force
  echo "✅ History squashed and force-pushed."
else
  git commit -m "$COMMIT_MESSAGE"

  echo "🚀 Pushing to main..."
  if git push "$REMOTE_REPO" HEAD:main; then
    echo "✅ Pushed successfully."
  else
    echo "⚠️ Push failed — check branch protection rules."
    exit 1
  fi
fi