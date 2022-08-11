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
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                ans.append(nums)
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  # backtrack

        n = len(nums)
        ans = []
        backtrack()
        return ans


print(_().permute([1, 2, 3]))
