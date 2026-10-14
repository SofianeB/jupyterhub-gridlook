#!/usr/bin/env bash
set -euo pipefail

REF="${GRIDLOOK_REF:-v1.6.1}"          # pin a tag from github.com/d70-t/gridlook/releases
HERE="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

git clone --depth 1 --branch "$REF" https://github.com/d70-t/gridlook.git "$WORK/gridlook"
cd "$WORK/gridlook"
node --version                         # repo wants >=24.16
npm ci
npm run build -- --base=./

rm -rf "$HERE/jupyterhub_gridlook/static"
mkdir -p "$HERE/jupyterhub_gridlook/static"
cp -r dist/. "$HERE/jupyterhub_gridlook/static/"
cp LICENSE "$HERE/jupyterhub_gridlook/static/LICENSE.gridlook"   # Gridlook is MIT; keep its notice
echo "built Gridlook $REF"