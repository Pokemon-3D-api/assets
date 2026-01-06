#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Define commit message
COMMIT_MESSAGE="Auto-update🤖: Optimized models and handled errors"

# 1) Configure a valid Git identity
git config --global user.name "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"

# 2) Construct Authenticated Remote URL
# This uses the env variables passed from the workflow
REMOTE_REPO="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

# 3) Check for any changes
if [[ -n $(git status --porcelain) ]]; then
  echo "Changes detected🔍, committing and pushing to main branch..."

  # Add all changes
  git add .

  # Commit with a message
  git commit -m "$COMMIT_MESSAGE"

  # 4) Try pushing to main
  # We push directly to the authenticated URL to bypass 403 errors
  if git push "$REMOTE_REPO" HEAD:main; then
    echo "✅ Changes successfully committed and pushed to main."
  else
    # 5) If push to main fails (branch protection?), create a new branch and push
    echo "❌ Failed to push to main. Creating new branch 'auto-updates'..."
    NEW_BRANCH="auto-updates"
    
    # Push the current state to the new branch on the remote
    if git push "$REMOTE_REPO" HEAD:"$NEW_BRANCH"; then
       echo "🫸🏻 Changes pushed to branch '$NEW_BRANCH'."
    else
       echo "🚨 Critical failure: Could not push to main or $NEW_BRANCH."
       exit 1
    fi
  fi
else
  echo "✨ No changes to commit."
fi