#!/usr/bin/env bash
set -eou pipefail
ty leetcode.py
git add ./schemas/*
git add -u
git commit -u -m "300"
git push
