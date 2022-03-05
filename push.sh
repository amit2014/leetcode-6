#!/usr/bin/env bash
set -eou pipefail
git add leetcode.sql
git commit leetcode.sql -m "SELECT 'em all, Leetcodemon!"
git push
