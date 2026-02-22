#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
APK_PATH="$ROOT_DIR/dist/dreampulse-preview-debug.apk"
TAG="${1:-v0.1.0}"
TITLE="${2:-DreamPulse Preview APK ${TAG}}"
NOTES="${3:-Offline preview APK build.}"

if [[ -z "${GITHUB_REPOSITORY:-}" ]]; then
  echo "GITHUB_REPOSITORY is required. Example: export GITHUB_REPOSITORY=owner/repo"
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) not found. Install from https://cli.github.com/"
  exit 1
fi

if [[ ! -f "$APK_PATH" ]]; then
  echo "APK not found at $APK_PATH. Building first..."
  bash "$ROOT_DIR/scripts/build_android_apk.sh"
fi

if ! gh auth status >/dev/null 2>&1; then
  if [[ -z "${GITHUB_TOKEN:-}" ]]; then
    echo "Please run 'gh auth login' or export GITHUB_TOKEN first."
    exit 1
  fi
  echo "$GITHUB_TOKEN" | gh auth login --with-token
fi

if gh release view "$TAG" --repo "$GITHUB_REPOSITORY" >/dev/null 2>&1; then
  gh release upload "$TAG" "$APK_PATH" --repo "$GITHUB_REPOSITORY" --clobber
else
  gh release create "$TAG" "$APK_PATH" \
    --repo "$GITHUB_REPOSITORY" \
    --title "$TITLE" \
    --notes "$NOTES"
fi

URL="https://github.com/${GITHUB_REPOSITORY}/releases/tag/${TAG}"
echo "Release URL: $URL"
