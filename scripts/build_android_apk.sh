#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
APK_SRC="$ROOT_DIR/android-app/app/build/outputs/apk/debug/app-debug.apk"
OUT_DIR="$ROOT_DIR/dist"

export ANDROID_SDK_ROOT="${ANDROID_SDK_ROOT:-$HOME/android-sdk}"
export ANDROID_HOME="$ANDROID_SDK_ROOT"

if [[ ! -d "$ANDROID_SDK_ROOT" ]]; then
  echo "Android SDK not found at $ANDROID_SDK_ROOT"
  echo "Please install command line tools and required platforms first."
  exit 1
fi

if ! command -v gradle >/dev/null 2>&1; then
  echo "gradle command not found. Please install Gradle 8.x first."
  exit 1
fi

printf 'sdk.dir=%s\n' "$ANDROID_SDK_ROOT" > "$ROOT_DIR/android-app/local.properties"

if command -v mise >/dev/null 2>&1; then
  mise exec java@17 -- gradle -p "$ROOT_DIR/android-app" --no-daemon assembleDebug
else
  gradle -p "$ROOT_DIR/android-app" --no-daemon assembleDebug
fi

mkdir -p "$OUT_DIR"
cp "$APK_SRC" "$OUT_DIR/dreampulse-preview-debug.apk"
sha256sum "$OUT_DIR/dreampulse-preview-debug.apk"
echo "APK ready: $OUT_DIR/dreampulse-preview-debug.apk"
