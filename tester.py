import re
from bisect import *  # type:ignore
from collections import *  # type:ignore
from functools import *  # type:ignore
from heapq import *  # type:ignore
from itertools import *  # type:ignore
from math import *  # type:ignore
from typing import *  # type:ignore

from structures import LinkedList, ListNode


class _:
    def check(self, s: str, w: str) -> bool:
        i, j = 0, 0
        for i in range(len(s)):
            if j < len(w) and s[i] == w[j]:
                j += 1
            elif s[i - 1 : i + 2] != s[i] * 3 != s[i - 2 : i + 1]:
                return False
        return j == len(w)

    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum(self.check(s, w) for w in words)


print(_().expressiveWords("aaa", ["aaaa"]))
