#!/usr/bin/env bash
set -xeou pipefail
echo + ry main.py
ry main.py
git add -u
git commit -u -m "75"
git push
