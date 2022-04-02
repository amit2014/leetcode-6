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
    def summaryRanges(self, nums):
        ans: List[str] = []
        i = 0
        while i < len(nums):
            begin = end = i
            while end < len(nums) - 1 and nums[end] + 1 == nums[end + 1]:
                end += 1
            ans.append(str(nums[begin]) + (("->" + str(nums[end])) * (begin != end)))
            i = end + 1
        return ans
