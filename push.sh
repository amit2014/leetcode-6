#!/usr/bin/env bash
set -eou pipefail
git add leetcode.sql
git add ./schemas/*
git commit -u -m "SELECT 'em all, Leetcodemon!"
git push
