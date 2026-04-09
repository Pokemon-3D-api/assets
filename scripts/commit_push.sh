#!/bin/bash
set -e 

COMMIT_MESSAGE="chore: asset sync & optimization 🐉✨"
MAX_COMMITS=5
REMOTE_REPO="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

git config --global user.name "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"

echo "🧹 Cleaning temporary raw files..."
rm -rf models/glb/*

if [[ -n $(git status --porcelain) ]]; then
  echo "🔍 Changes detected. Preparing to update repo..."

  git add models/opt/ scripts/model_map.json

  COUNT=$(git rev-list --count HEAD)
  echo "📊 Current commit count: $COUNT"

  if [ "$COUNT" -gt "$MAX_COMMITS" ]; then
    echo "📉 Pruning history (Squashing to clean slate) to save space..."
    git checkout --orphan temp_branch
    git add -A
    git commit -m "chore: re-synced assets (clean slate) 💎"
    git branch -D main
    git branch -m main
    
    git push "$REMOTE_REPO" main --force
    echo "✅ History squashed and pushed successfully."
  else
    git commit -m "$COMMIT_MESSAGE"
    
    if git push "$REMOTE_REPO" HEAD:main; then
      echo "✅ Changes pushed to main."
    else
      echo "⚠️ Push failed. Check for branch protection or sync issues."
      exit 1
    fi
  fi
else
  echo "✨ No changes to commit. Everything is up to date."
fi