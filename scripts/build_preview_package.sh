#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT_DIR/dist"
PKG_NAME="dreampulse-preview-mobile-test.zip"

mkdir -p "$OUT_DIR"
cd "$ROOT_DIR/preview"
zip -qr "$OUT_DIR/$PKG_NAME" .

echo "Built package: $OUT_DIR/$PKG_NAME"
