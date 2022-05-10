#!/usr/bin/env bash
set -eou pipefail

filepath=''
if [[ $# -eq 0 ]]; then
    filepath='leetcode.cpp'
else
    filepath=$1
fi

# clang-format -i --style="{IndentWidth: 4}" filepath
clang-format -i --style="Google" $filepath
py -m cpplint --filter=-legal/copyright,-build/include_subdir,-runtime/references $filepath
g++ -std=c++17 $filepath -o __DELETE
rm __DELETE
