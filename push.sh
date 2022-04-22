#!/usr/bin/env bash
set -xeou pipefail
ty leetcode.py
git add -u
git commit -u -m "300"
git push
