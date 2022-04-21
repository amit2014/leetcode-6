#!/usr/bin/env bash
set -eou pipefail
clang-format -i --style="{IndentWidth: 4}" leetcode.cpp
py -m cpplint --filter=-legal/copyright,-build/include_subdir,-runtime/references leetcode.cpp
g++ -std=c++17 leetcode.cpp -o __DELETE
rm __DELETE
