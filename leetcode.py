"""Top 300ish leetcode algorithm questions by frequencyish."""

from __future__ import annotations

import datetime
import re
from bisect import bisect_left
from collections import Counter, OrderedDict, defaultdict, deque
from functools import lru_cache, reduce
from heapq import heapify, heappop, heappush, nlargest
from itertools import chain, groupby, permutations, product, zip_longest
from math import comb, inf, sqrt
from random import choice, random, shuffle
from typing import Callable, Deque, Dict, Final, List, Optional, Set, Tuple, Union

#########################################################################################
# - Common -

TrieNodeType = Dict[str, "TrieNodeType"]
DefaultDictTrie: Callable[[], TrieNodeType] = lambda: defaultdict(DefaultDictTrie)


class ListNode:
    def __init__(
        self,
        key: int = 0,
        val: int = 0,
        prev: Optional[ListNode] = None,
        next: Optional[ListNode] = None,
    ):
        self.key = key  # TODO I don't need this
        self.val = val
        self.prev = prev
        self.next = next


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional[Node] = None,
        right: Optional[Node] = None,
        parent: Optional[Node] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class UnionFind:
    def __init__(self, n: int, count: int):
        """O(n) space"""
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = count

    def find(self, A: int) -> int:
        """O(inverse Ackermann function) time"""
        while self.parent[A] != A:
            A, self.parent[A] = self.parent[A], self.parent[self.parent[A]]
        return A

    def union(self, A: int, B: int) -> bool:
        """O(inverse Ackermann function) time
        True if a merge happened, False otherwise"""
        root_A = self.find(A)
        root_B = self.find(B)

        if root_A == root_B:
            return False

        if self.size[root_A] < self.size[root_B]:
            root_A, root_B = root_B, root_A

        self.parent[root_B] = root_A
        self.size[root_A] += self.size[root_B]

        self.count -= 1
        return True


#########################################################################################
# - Placeholders -


def isBadVersion(version: int) -> bool:
    ...


# NOTE we ended up type: ignore'ing all the type errors that came from this
#      ??\_(???)_/??
class NestedInteger:
    def __init__(self, value: Optional[int] = None):
        ...

    def isInteger(self) -> bool:
        ...

    def add(self, elem: Union[int, NestedInteger]) -> None:
        ...

    def setInteger(self, value: int) -> None:
        ...

    def getInteger(self) -> Optional[int]:
        ...

    def getList(self) -> Optional[List[NestedInteger]]:
        ...


#########################################################################################


class _1:
    """
    # - Two Sum -
    # https://leetcode.com/problems/two-sum/
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.

    You can return the answer in any order.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """O(n) time, O(n) space"""
        seen: Dict[int, int] = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
        raise RuntimeError("No two distinct integers sum to target!")


class _146:
    """
    # - LRU Cache -
    # https://leetcode.com/problems/lru-cache/
    Design a data structure that follows the constraints of a Least Recently
    Used (LRU) cache.

    Implement the LRUCache class:
        - `LRUCache(int capacity)` Initialize the LRU cache with positive
            size capacity.
        - `int get(int key)` Return the value of the key if the key exists,
            otherwise return -1.
        - `void put(int key, int value)` Update the value of the key if the
            key exists. Otherwise, add the key-value pair to the cache. If
            the number of keys exceeds the capacity from this operation,
            evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.

    Example 1:
    Input
    ["LRUCache", "put" , "put" , "get", "put" , "get", "put" , "get", "get", "get"]
    [[2]       , [1, 1], [2, 2], [1]  , [3, 3], [2]  , [4, 4], [1]  , [3]  , [4]  ]
    Output
    [null      , null  , null  , 1    , null  , -1   , null  , -1   , 3    , 4    ]

    Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
    """

    class LRUCache:
        def __init__(self, capacity: int):
            """O(n) space"""
            assert capacity > 0
            self.capacity = capacity
            self.mp: Dict[int, ListNode] = {}  # hash table
            self.head = ListNode()  # doubly linked list
            self.tail = ListNode()
            self.head.next = self.tail
            self.tail.prev = self.head

        def _delete(self, key: int) -> int:
            node = self.mp.pop(key)
            assert node.prev is not None and node.next is not None
            node.prev.next = node.next
            node.next.prev = node.prev
            return node.val

        def _insert(self, key: int, value: int) -> None:
            node = ListNode(key, value, self.tail.prev, self.tail)
            assert node.prev is not None and node.next is not None
            self.tail.prev.next = self.tail.prev = node  # insert at tail
            self.mp[key] = node

        def get(self, key: int) -> int:
            """O(1) time"""
            if key not in self.mp:
                return -1
            value = self._delete(key)
            self._insert(key, value)
            return value

        def put(self, key: int, value: int) -> None:
            """O(1) time"""
            assert self.head.next is not None
            if key in self.mp:
                self._delete(key)
            self._insert(key, value)
            if len(self.mp) > self.capacity:
                self._delete(self.head.next.key)


class _56:
    """
    # - Merge Intervals -
    # https://leetcode.com/problems/merge-intervals/
    Given an array of intervals where intervals[i] = [starti, endi], merge all
    overlapping intervals, and return an array of the non-overlapping intervals
    that cover all the intervals in the input.

    Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans: List[List[int]] = []
        for x, y in sorted(intervals, key=lambda x: x[1]):
            # think: "if the ends are sorted,
            # just worry about the starts"
            while ans and x <= ans[-1][1]:  # e.g. [[1,2],[3,6]] <-merge- [4,7]
                x = min(x, ans.pop()[0])
            ans.append([x, y])
        return ans


class _423:
    """
    # - Reconstruct Original Digits from English -
    # https://leetcode.com/problems/reconstruct-original-digits-from-english/
    Given a string s containing an out-of-order English representation of digits
    0-9, return the digits in ascending order.

    Example 1:
    Input: s = "owoztneoer"
    Output: "012"

    Example 2:
    Input: s = "fviefuro"
    Output: "45"

    NOTE s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u",
    "t","w","v","x","z"].
    NOTE s is guaranteed to be valid.
    """

    def originalDigits(self, s: str) -> str:
        count: Dict[str, int] = Counter(s)
        out: Dict[int, int] = {}
        # letter "z" is present only in "zero"
        out[0] = count["z"]
        # letter "w" is present only in "two"
        out[2] = count["w"]
        # letter "u" is present only in "four"
        out[4] = count["u"]
        # letter "x" is present only in "six"
        out[6] = count["x"]
        # letter "g" is present only in "eight"
        out[8] = count["g"]
        # letter "h" is present only in "three" and "eight"
        out[3] = count["h"] - out[8]
        # letter "f" is present only in "five" and "four"
        out[5] = count["f"] - out[4]
        # letter "s" is present only in "seven" and "six"
        out[7] = count["s"] - out[6]
        # letter "i" is present in "nine", "five", "six", and "eight"
        out[9] = count["i"] - out[5] - out[6] - out[8]
        # letter "n" is present in "one", "nine", and "seven"
        out[1] = count["n"] - out[7] - 2 * out[9]
        return "".join([str(key) * out[key] for key in sorted(out.keys())])


class _42:
    """
    # - Trapping Rain Water -
    # https://leetcode.com/problems/trapping-rain-water/
    Given n non-negative integers representing an elevation map where the width of
    each bar is 1, compute how much water it can trap after raining.

    Example 1:
    3|       X
    2|   X   XX X
    1|_X_XX_XXXXXX

    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array
    [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
    are being trapped.

    Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9
    """

    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max = r_max = area = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] < l_max:
                    area += l_max - height[l]
                else:
                    l_max = height[l]
                l += 1
            else:
                if height[r] < r_max:
                    area += r_max - height[r]
                else:
                    r_max = height[r]
                r -= 1
        return area


class _200:
    """
    # - Number of Islands -
    # https://leetcode.com/problems/number-of-islands/
    Given an m x n 2D binary grid grid which represents a map of '1's (land)
    and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are
    all surrounded by water.

    Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

    Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS method, O(mn) time and space
        def fn(i, j, grid: List[List[str]]) -> None:
            """Flood island with 0s."""
            if (
                i < 0
                or j < 0
                or i == len(grid)
                or j == len(grid[0])
                or grid[i][j] == "0"
            ):
                return
            else:
                grid[i][j] = "0"
            fn(i, j + 1, grid)
            fn(i, j - 1, grid)
            fn(i + 1, j, grid)
            fn(i - 1, j, grid)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    fn(i, j, grid)
        return islands

    """
    index = i * n + j
    1 1
    1 0

    0,0 0,1
    1,0 1,1

    0*2+0 0*2+1    0 1
    1*2+0 1*2+1    2 3
    """

    def numIslands_(self, grid: List[List[str]]) -> int:
        # UnionFind method, O(mn) time and space
        # but each operation takes O(inverse Ackermann function) time
        # which is essentially O(1), thus superior to DFS
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        count = sum(grid[i][j] == "1" for i in range(m) for j in range(n))
        uf = UnionFind(m * n, count)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                index = i * n + j
                if j < n - 1 and grid[i][j + 1] == "1":
                    uf.union(index, index + 1)
                if i < m - 1 and grid[i + 1][j] == "1":
                    uf.union(index, index + n)
        return uf.count


class _4:
    """
    # - Median of Two Sorted Arrays -
    # https://leetcode.com/problems/median-of-two-sorted-arrays/
    Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

    Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    """

    # https://www.youtube.com/watch?v=LPFhl65R7ww
    # https://github.com/mission-peace/interview/blob/master/src/com/interview/binarysearch/MedianOfTwoSortedArrayOfDifferentLength.java

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """O(log(min(m,n)) time, O(m+n) space"""
        x, y = sorted((nums1, nums2), key=len)
        low, high = 0, len(x)

        while low <= high:
            x_partition = (low + high) // 2
            y_partition = (len(x) + len(y) + 1) // 2 - x_partition

            # four points of interest about the two partitions
            max_l_x = x[x_partition - 1] if x_partition > 0 else -inf
            max_l_y = y[y_partition - 1] if y_partition > 0 else -inf

            min_r_x = x[x_partition] if x_partition < len(x) else inf
            min_r_y = y[y_partition] if y_partition < len(y) else inf

            if max_l_x <= min_r_y and max_l_y <= min_r_x:  # valid partition
                if (len(x) + len(y)) % 2 == 0:  # even
                    return (max(max_l_x, max_l_y) + min(min_r_x, min_r_y)) / 2
                else:  # odd
                    return max(max_l_x, max_l_y)
            # binary search
            elif max_l_x > min_r_y:
                high = x_partition - 1
            else:
                low = x_partition + 1
        raise RuntimeError("Couldn't find median of two sorted arrays!")


class _121:
    """
    # - Best Time to Buy and Sell Stock -
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    You are given an array prices where prices[i] is the price of a given stock
    on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you
    cannot achieve any profit, return 0.

    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
    profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you
    must buy before you sell.

    Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
    """

    def maxProfit(self, prices: List[int]) -> int:
        """O(n) time, O(1) space"""
        buy, profit = prices[0], 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit


class _1249:
    """
    # - Minimum Remove to Make Valid Parentheses -
    # https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ('(' or ')', in
    any positions) so that the resulting parentheses string is valid and
    return any valid string.

    Formally, a parentheses string is valid if and only if:
        - It is the empty string, contains only lowercase characters, or
        - It can be written as AB (A concatenated with B), where A and B are
          valid strings, or
        - It can be written as (A), where A is a valid string.

    Example 1:
    Input: s = "lee(t(c)o)de)"
    Output:    "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

    Example 2:
    Input: s = "a)b(c)d"
    Output:    "ab(c)d"

    Example 3:
    Input: s = "))(("
    Output:    ""
    Explanation: An empty string is also valid.
    """

    def minRemoveToMakeValid(self, s: str) -> str:
        """O(n) time and space"""
        list_s = list(s)
        stack: List[int] = []
        for i, c in enumerate(list_s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:  # matching
                    stack.pop()
                else:  # extra
                    list_s[i] = ""
        while stack:
            list_s[stack.pop()] = ""
        return "".join(list_s)


class _20:
    """
    # - Valid Parentheses -
    # https://leetcode.com/problems/valid-parentheses/
    Given a string s containing just the characters '(', ')', '{', '}',
    '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Example 1:
    Input: s = "()"
    Output: true

    Example 2:
    Input: s = "()[]{}"
    Output: true

    Example 3:
    Input: s = "(]"
    Output: false
    """

    def isValid(self, s: str) -> bool:
        """O(n) time and space"""
        stack: List[str] = []
        match = {"(": ")", "[": "]", "{": "}"}
        for x in s:
            if x in match:
                stack.append(x)
            elif not stack or match[stack.pop()] != x:
                return False
        return not stack


class _53:
    """
    # - Maximum Subarray -
    # https://leetcode.com/problems/maximum-subarray/
    Given an integer array nums, find the contiguous subarray (containing at
    least one number) which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.

    Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

    Example 2:
    Input: nums = [1]
    Output: 1

    Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    """

    def maxSubArray(self, nums: List[int]) -> int:
        """O(n) time, O(1) space"""
        cur = ans = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            ans = max(ans, cur)
        return ans


class _68:
    """
    # - Text Justification -
    # https://leetcode.com/problems/text-justification/
    Given an array of strings words and a width maxWidth, format the text
    such that each line has exactly maxWidth characters and is fully (left
    and right) justified.

    You should pack your words in a greedy approach; that is, pack as many
    words as you can in each line. Pad extra spaces ' ' when necessary so
    that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible.
    If the number of spaces on a line does not divide evenly between words,
    the empty slots on the left will be assigned more spaces than the
    slots on the right.

    For the last line of text, it should be left-justified and no extra
    space is inserted between words.

    Note:
        - A word is defined as a character sequence consisting of non-space
        characters only.
        - Each word's length is guaranteed to be greater than 0 and not
        exceed maxWidth.
        - The input array words contains at least one word.

    Example 1:
    Input: words = ["This", "is", "an", "example", "of", "text", "justification."],
    maxWidth = 16
    Output:
    [
    "This    is    an",
    "example  of text",
    "justification.  "
    ]

    Example 2:
    Input: words = ["What","must","be","acknowledgment","shall","be"],
    maxWidth = 16
    Output:
    [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be",
    because the last line must be left-justified instead of fully-justified.
    Note that the second line is also left-justified becase it contains only one word.

    Example 3:
    Input: words = ["Science","is","what","we","understand","well","enough",
    "to","explain","to","a","computer.","Art","is","everything","else","we","do"],
    maxWidth = 20
    Output:
    [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
    ]
    """

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans: List[str] = []
        line: List[str] = []
        width = 0

        for word in words:
            if width + len(line) + len(word) > maxWidth:
                q, r = divmod(maxWidth - width, max(1, len(line) - 1))
                for i in range(max(1, len(line) - 1)):
                    line[i] += " " * (q + (i < r))
                ans.append("".join(line))
                line, width = [], 0
            line.append(word)
            width += len(word)

        ans.append(" ".join(line).ljust(maxWidth))
        return ans


class _3:
    """
    # - Longest Substring Without Repeating Characters -
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Given a string s, find the length of the longest substring without repeating
    characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a
    substring.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        mp: Dict[str, int] = {}  # char -> highest_string_idx
        ans = i = 0
        for j in range(len(s)):
            char = s[j]
            if char in mp:
                i = max(i, mp[char] + 1)
            ans = max(ans, j - i + 1)
            mp[char] = j
        return ans


class _815:
    """
    # - Bus Routes -
    # https://leetcode.com/problems/bus-routes/
    You are given an array routes representing bus routes where routes[i] is a
    bus route that the ith bus repeats forever. For example, if
    routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence
    1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever. You will start at the bus
    stop source (You are not on any bus initially), and you want to go to the
    bus stop target. You can travel between bus stops by buses only. Return the
    least number of buses you must take to travel from source to target. Return
    -1 if it is not possible.

    Example 1:
    Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
    Output: 2
    Explanation: The best strategy is take the first bus to the bus stop 7,
                    then take the second bus to the bus stop 6.

    Example 2:
    Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
    Output: -1

    NOTE All the values of routes[i] are unique.
    """

    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        mp: Dict[int, Set[int]] = defaultdict(set)  # {stop:set(bus#)}
        for bus, stops in enumerate(routes):
            for stop in stops:
                mp[stop].add(bus)

        # deque([(stop,bus_count)])
        queue: Deque[Tuple[int, int]] = deque([(source, 0)])
        visited_stops: Set[int] = set()
        visited_buses: Set[int] = set()
        while queue:
            stop, count = queue.popleft()
            if stop == target:
                return count
            for bus in mp[stop]:
                if bus not in visited_buses:  # prevent loop
                    visited_buses.add(bus)
                    for stop in routes[bus]:
                        if stop not in visited_stops:  # prevent loop again
                            visited_stops.add(stop)
                            queue.append((stop, count + 1))
        return -1


class _588:
    """
    # - Design In-Memory File System -
    # https://leetcode.com/problems/design-in-memory-file-system/
    Design a data structure that simulates an in-memory file system.

    Implement the FileSystem class:
    - FileSystem() Initializes the object of the system.
    - List<String> ls(String path)
        - If path is a file path, returns a list that only contains this file's
        name.
        - If path is a directory path, returns the list of file and directory
        names in this directory.
    The answer should in lexicographic order.
    - void mkdir(String path) Makes a new directory according to the given path.
    The given directory path does not exist. If the middle directories in the
    path do not exist, you should create them as well.
    - void addContentToFile(String filePath, String content)
        - If filePath does not exist, creates that file containing given content.
        - If filePath already exists, appends the given content to original content.
    - String readContentFromFile(String filePath) Returns the content in the file
    at filePath.

    Input
    ["FileSystem", "ls" , "mkdir"   , "addContentToFile"   , "ls"    , "readContentFromFile"]
    [[]          , ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"]   , ["/a/b/c/d"]]
    Output
    [null        , []   , null      , null                 , ["a"]   , "hello"]

    Explanation
    FileSystem fileSystem = new FileSystem();
    fileSystem.ls("/");                         // return []
    fileSystem.mkdir("/a/b/c");
    fileSystem.addContentToFile("/a/b/c/d", "hello");
    fileSystem.ls("/");                         // return ["a"]
    fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
    """

    class FileSystem:
        def __init__(self) -> None:
            self.file_tree = DefaultDictTrie()  # TODO fix type hint
            self.files: Dict[str, str] = defaultdict(str)

        def ls(self, path: str) -> List[str]:
            if path in self.files:
                return path.split("/")[-1:]  # returns the last item as a List
            path_node = self.file_tree
            for token in path.split("/"):
                if token in path_node:
                    path_node = path_node[token]
                elif token:
                    return []
            return sorted(path_node.keys())

        def mkdir(self, path: str) -> None:
            path_node = self.file_tree
            for token in path.split("/"):
                if token:
                    path_node = path_node[token]

        def addContentToFile(self, file_path: str, content: str) -> None:
            self.mkdir(file_path)
            self.files[file_path] += content

        def readContentFromFile(self, file_path: str) -> str:
            return self.files[file_path]


class _253:
    """
    # - Meeting Rooms II -
    # https://leetcode.com/problems/meeting-rooms-ii/
    Given an array of meeting time intervals intervals where intervals[i] =
    [starti, endi], return the minimum number of conference rooms required.

    Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2

    Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: 1
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """O(nlogn) time O(n) space"""
        if not intervals:
            return 0

        free_rooms = []  # heaps
        intervals.sort(key=lambda x: x[0])
        heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heappop(free_rooms)
            heappush(free_rooms, i[1])
        return len(free_rooms)


class _680:
    """
    # - Valid Palindrome II -
    # https://leetcode.com/problems/valid-palindrome-ii/
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.

    Example 1:

    Input: s = "aba"
    Output: true
    Example 2:

    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.
    Example 3:

    Input: s = "abc"
    Output: false

    Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    """

    def validPalindrome(self, s: str) -> bool:
        """O(n) time O(1) space"""

        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        return True


class _1235:
    """
    # - Maximum Profit in Job Scheduling -
    # https://leetcode.com/problems/maximum-profit-in-job-scheduling/
    """

    ...


# TODO I dont think i actually finished understanding this one redo
class _31:
    """
    # - Next Permutation -
    # https://leetcode.com/problems/next-permutation/
    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
    Given an array of integers nums, find the next permutation of nums.

    The replacement must be in place and use only constant extra memory.

    Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]

    Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]

    Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]
    """

    def nextPermutation(self, nums: List[int]) -> None:
        k = len(nums) - 1
        while k and nums[k - 1] >= nums[k]:
            k -= 1

        if k:
            lo, hi = k, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= nums[k - 1]:
                    hi = mid
                else:
                    lo = mid + 1
            nums[k - 1], nums[lo - 1] = nums[lo - 1], nums[k - 1]

        lo, hi = k, len(nums) - 1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo + 1, hi - 1


class _15:
    """
    # - 3Sum -
    # https://leetcode.com/problems/3sum/
    Given an integer array nums, return all the triplets [nums[i], nums[j],
    nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
    nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Example 2:
    Input: nums = []
    Output: []

    Example 3:
    Input: nums = [0]
    Output: []
    """

    ...


class _528:
    """
    # - Random Pick with Weight -
    # https://leetcode.com/problems/random-pick-with-weight/
    You are given a 0-indexed array of positive integers w where w[i] describes the
    weight of the ith index.

    You need to implement the function pickIndex(), which randomly picks an index in the
    range [0, w.length - 1] (inclusive) and returns it. The probability of picking an
    index i is w[i] / sum(w).

    For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25
    (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%)

    Example 1:
    Input
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output
    [null,0]
    Explanation
    Solution solution = new Solution([1]);
    solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

    Example 2:
    Input
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    Output
    [null,1,1,1,1,0]
    Explanation
    Solution solution = new Solution([1, 3]);
    solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 1
    solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

    Since this is a randomization problem, multiple answers are allowed.
    All of the following outputs can be considered correct:
    [null,1,1,1,1,0]
    [null,1,1,1,1,1]
    [null,1,1,1,0,0]
    [null,1,1,1,0,1]
    [null,1,0,1,0,0]
    ......
    and so on.
    """

    # NOTE worst problem description on leetcode

    class Solution:
        def __init__(self, w: List[int]):
            self.prefix_sums = []
            prefix_sum = 0
            for weight in w:
                prefix_sum += weight
                self.prefix_sums.append(prefix_sum)
            self.total_sum = prefix_sum

        def pickIndex(self) -> int:
            # NOTE you must from random import random on leetcode
            target = self.total_sum * random()
            low, high = 0, len(self.prefix_sums)
            while low < high:
                mid = (low + high) // 2
                if target > self.prefix_sums[mid]:
                    low = mid + 1
                else:
                    high = mid
            return low


class _5:
    """
    # - Longest Palindromic Substring -
    # https://leetcode.com/problems/longest-palindromic-substring/
    """


class _380:
    """
    # - Insert Delete GetRandom O(1) -
    # https://leetcode.com/problems/insert-delete-getrandom-o1/
    """

    ...


class _2:
    """
    # - Add Two Numbers -
    # https://leetcode.com/problems/add-two-numbers/
    """

    ...


class _560:
    """
    # - Subarray Sum Equals K -
    # https://leetcode.com/problems/subarray-sum-equals-k/
    Given an array of integers nums and an integer k, return the total number of
    subarrays whose sum equals to k.

    Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

    Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2
    """

    # NOTE this one is simple, but I don't fully gronk it

    def subarraySum(self, nums: List[int], k: int) -> int:
        """O(n) time O(n) space"""
        count = sum = 0
        mp: Dict[int, int] = {0: 1}  # {sum: count of sum}
        for num in nums:
            sum += num
            if sum - k in mp:
                count += mp[sum - k]
            mp[sum] = mp.get(sum, 0) + 1
        return count


class _811:
    """
    # - Subdomain Visit Count -
    # https://leetcode.com/problems/subdomain-visit-count/
    """

    ...


class _314:
    """
    # - Binary Tree Vertical Order Traversal -
    # https://leetcode.com/problems/binary-tree-vertical-order-traversal/
    Given the root of a binary tree, return the vertical order traversal of its node's
    values. (i.e., from top to bottom, column by column).

    If two nodes are in the same row and column, the order should be from left to right.

    Example 1:
             3
       9           20
                15    7
    Input: root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]

    Example 2:
             3
       9           8
    4     0     1     7
    Input: root = [3,9,8,4,0,1,7]
    Output: [[4],[9],[3,0,1],[8],[7]]

    Example 3:
                         3
             9                       8
       4           0           1           7
                      2     5
    Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
    Output: [[4],[9,5],[3,0,1],[8,2],[7]]
    """

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """O(nlogn) time O(n) space"""
        ans = defaultdict(list)
        queue: List[Tuple[Optional[TreeNode], int]] = [(root, 0)]
        for node, k in queue:
            if node:
                ans[k].append(node.val)
                queue.append((node.left, k - 1))
                queue.append((node.right, k + 1))
        return [ans[k] for k in sorted(ans)]

    def verticalOrder_(self, root: TreeNode) -> List[List[int]]:
        """O(n) time O(n) space"""
        if root is None:
            return []
        ans = defaultdict(list)
        min_ = max_ = 0
        queue: Deque[Tuple[Optional[TreeNode], int]] = deque([(root, 0)])
        while queue:
            node, k = queue.popleft()
            if node:
                ans[k].append(node.val)
                min_ = min(min_, k)
                max_ = max(max_, k)
                queue.append((node.left, k - 1))
                queue.append((node.right, k + 1))
        return [ans[k] for k in range(min_, max_ + 1)]


class _394:
    """
    # - Decode String -
    # https://leetcode.com/problems/decode-string/
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square
    brackets is being repeated exactly k times. Note that k is guaranteed to be a
    positive integer.

    You may assume that the input string is always valid; there are no extra white
    spaces, square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any digits and
    that digits are only for those repeat numbers, k. For example, there will not be
    input like 3a or 2[4].

    Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

    NOTE s consists of lowercase English letters, digits, and square brackets '[]'.
    NOTE s is guaranteed to be a valid input.
    """

    def decodeString(self, s: str) -> str:
        stack: List[Union[str, int]] = []
        curNum, curString = 0, ""
        for c in s:
            if c == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif c == "]":
                num = stack.pop()
                assert isinstance(num, int)
                prevString = stack.pop()
                assert isinstance(prevString, str)
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString


class _1396:
    """
    # - Design Underground System -
    # https://leetcode.com/problems/design-underground-system/
    """

    ...


class _236:
    """
    # - Lowest Common Ancestor of a Binary Tree -
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
    Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

    Each node will have a reference to its parent node. The definition for Node is below:
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node parent;
    }
    According to the definition of LCA on Wikipedia: "The lowest common ancestor of two
    nodes p and q in a tree T is the lowest node that has both p and q as descendants
    (where we allow a node to be a descendant of itself)."

    Example 1:
                         3
             5                       1
       6           2           0           8
                7     4
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

    Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

    Example 3:
       1
    2
    Input: root = [1,2], p = 1, q = 2
    Output: 1

    Constraints:
    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q exist in the tree.
    """

    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        path = set()
        while p:
            path.add(p)
            p = p.parent  # type: ignore
        while q not in path:
            q = q.parent  # type: ignore
        return q


class _215:
    """
    # - Kth Largest Element in an Array -
    # https://leetcode.com/problems/kth-largest-element-in-an-array/
    Given an integer array nums and an integer k, return the kth largest element in
    the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct
    element.

    Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
    """

    # NOTE Quickselect uses the same overall approach as quicksort, choosing one element as a pivot and partitioning the data in two based on the pivot, accordingly as less than or greater than the pivot. However, instead of recursing into both sides, as in quicksort, quickselect only recurses into one side ??? the side with the element it is searching for. This reduces the average complexity from O(nlogn) to O(n), with a worst case of O(n^2).

    # TODO I only understand the recursive one
    # btw... these perform worse than
    #   return sorted(nums)[-k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Quickselect method recursive"""
        pivot = choice(nums)

        greater = [x for x in nums if x > pivot]
        equal = [x for x in nums if x == pivot]
        less = [x for x in nums if x < pivot]

        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k > len(greater) + len(equal):
            return self.findKthLargest(less, k - len(greater) - len(equal))
        else:
            return equal[0]

    def findKthLargest_(self, nums: List[int], k: int) -> int:
        """Quickselect method iterative"""

        def partition(lo, hi):
            """Return partition of nums[lo:hi]"""
            i, j = lo + 1, hi - 1
            while i <= j:
                if nums[i] < nums[lo]:
                    i += 1
                elif nums[j] > nums[lo]:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[lo], nums[j] = nums[j], nums[lo]
            return j

        shuffle(nums)
        lo, hi = 0, len(nums)
        while True:
            mid = partition(lo, hi)
            if mid + k < len(nums):
                lo = mid + 1
            elif mid + k == len(nums):
                return nums[mid]
            else:
                hi = mid


class _227:
    """
    # - Basic Calculator II -
    # https://leetcode.com/problems/basic-calculator-ii/
    """

    ...


class _273:
    """
    # - Integer to English Words -
    # https://leetcode.com/problems/integer-to-english-words/
    """

    ...


class _14:
    """
    # - Longest Common Prefix -
    # https://leetcode.com/problems/longest-common-prefix/
    """

    ...


class _23:
    """
    # - Merge k Sorted Lists -
    # https://leetcode.com/problems/merge-k-sorted-lists/
    """

    ...


class _134:
    """
    # - Gas Station -
    # https://leetcode.com/problems/gas-station/
    """

    ...


class _973:
    """
    # - K Closest Points to Origin -
    # https://leetcode.com/problems/k-closest-points-to-origin/
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y
    plane and an integer k, return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance
    (i.e., ???(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed to be unique
    (except for the order that it is in).

    Example 1:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

    Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: sqrt(x[0] ** 2 + x[1] ** 2))[:k]

    def kClosest_(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Quickselect iterative method"""
        left, right = 0, len(points) - 1
        pivot_index = -1
        while pivot_index != k:
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        return points[:k]

    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        pivot = points[(right + left) // 2]
        pivot_dist = self.squared_distance(pivot)
        while left < right:
            if self.squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left

    def squared_distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2


class _41:
    """
    # - First Missing Positive -
    # https://leetcode.com/problems/first-missing-positive/
    """

    ...


class _50:
    """
    # - Pow(x, n) -
    # https://leetcode.com/problems/powx-n/
    Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

    Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

    Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
    """

    def myPow(self, x: float, n: int) -> float:
        """O(logn) time, O(1) space"""
        if n < 0:
            x, n = 1 / x, -n
        ans = 1.0
        while n:
            if n & 1:
                ans *= x
            x, n = x * x, n // 2
        return ans


class _79:
    """
    # - Word Search -
    # https://leetcode.com/problems/word-search/
    Given an m x n grid of characters board and a string word, return true if
    word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring. The
    same letter cell may not be used more than once.

    Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    word = "ABCCED"
    Output: true

    Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    word = "SEE"
    Output: true

    Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    word = "ABCB"
    Output: false
    """

    ...


class _49:
    """
    # - Group Anagrams -
    # https://leetcode.com/problems/group-anagrams/
    Given an array of strings strs, group the anagrams together. You can return
    the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different
    word or phrase, typically using all the original letters exactly once.

    Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Example 2:
    Input: strs = [""]
    Output: [[""]]

    Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
    """

    ...


class _33:
    """
    # - Search in Rotated Sorted Array -
    # https://leetcode.com/problems/search-in-rotated-sorted-array/
    There is an integer array nums sorted in ascending order (with distinct
    values).

    Prior to being passed to your function, nums is possibly rotated at an
    unknown pivot index k (1 <= k < nums.length) such that the resulting array
    is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
    (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index
    3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    Example 3:
    Input: nums = [1], target = 0
    Output: -1
    """

    ...


class _22:
    """
    # - Generate Parentheses -
    # https://leetcode.com/problems/generate-parentheses/
    Given n pairs of parentheses, write a function to generate all combinations of
    well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
    Input: n = 1
    Output: ["()"]
    """

    # http://www.geometer.org/mathcircles/catalan.pdf
    """
    We know that in any zbalanced set, the first character has to be ???(???. We also know
    that somewhere in the set is the matching ???)??? for that opening one. In between that
    pair of parentheses is a balanced set of parentheses, and to the right of it is
    another balanced set:
        (A)B
    where A is a balanced set of parentheses and so is B. Both A and B can contain up to
    n - 1 pairs of parentheses, but if A contains k pairs, then B contains n - k - 1
    pairs. Notice that we will allow either A or B to contain zero pairs, and that there
    is exactly one way to do so: don't write down any parentheses.
    """

    @lru_cache(maxsize=None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ans = []
        for k in range(n):
            for x in self.generateParenthesis(n - k - 1):
                for y in self.generateParenthesis(k):
                    ans.append(f"({x}){y}")
        return ans


class _1570:
    """
    # - Dot Product of Two Sparse Vectors -
    # https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
    Given two sparse vectors, compute their dot product.

    Implement class SparseVector:
        - SparseVector(nums) Initializes the object with the vector nums
        - dotProduct(vec) Compute the dot product between the instance of
        SparseVector and vec

    A sparse vector is a vector that has mostly zero values, you should store the
    sparse vector efficiently and compute the dot product between two SparseVector.

    Follow up: What if only one of the vectors is sparse?

    Example 1:
    Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
    Output: 8
    Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
    v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

    Example 2:
    Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
    Output: 0
    Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
    v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

    Example 3:
    Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
    Output: 6
    """

    class SparseVector:
        """Index-value pair method: O(n) time, O(L) space
        n being the len(nums), L being the number of non-zero elements"""

        def __init__(self, nums: List[int]):
            self.pairs = []
            for i, num in enumerate(nums):
                if num != 0:
                    self.pairs.append([i, num])

        def dotProduct(self, vec: _1570.SparseVector) -> int:
            ans = 0
            p, q = 0, 0

            while p < len(self.pairs) and q < len(vec.pairs):
                if self.pairs[p][0] == vec.pairs[q][0]:
                    ans += self.pairs[p][1] * vec.pairs[q][1]
                    p += 1
                    q += 1
                elif self.pairs[p][0] < vec.pairs[q][0]:
                    p += 1
                else:
                    q += 1

            return ans

    class SparseVector_:
        """Hash set method: O(n) time, O(L) space
        n being the len(nums), L being the number of non-zero elements"""

        def __init__(self, nums: List[int]):
            self.m = {i: x for i, x in enumerate(nums) if x}

        def dotProduct(self, vec: _1570.SparseVector_) -> int:
            return sum(
                [x * y for i, x in self.m.items() for j, y in vec.m.items() if i == j]
            )


class _828:
    """
    # - Count Unique Characters of All Substrings of a Given String -
    # https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
    """

    ...


class _1762:
    """
    # - Buildings With an Ocean View -
    # https://leetcode.com/problems/buildings-with-an-ocean-view/
    There are n buildings in a line. You are given an integer array heights of
    size n that represents the heights of the buildings in the line.

    The ocean is to the right of the buildings. A building has an ocean view if
    the building can see the ocean without obstructions. Formally, a building
    has an ocean view if all the buildings to its right have a smaller height.

    Return a list of indices (0-indexed) of buildings that have an ocean view,
    sorted in increasing order.

    Example 1:
    Input: heights = [4,2,3,1]
    Output: [0,2,3]
    Explanation: Building 1 (0-indexed) does not have an ocean view because
    building 2 is taller.

    Example 2:
    Input: heights = [4,3,2,1]
    Output: [0,1,2,3]
    Explanation: All the buildings have an ocean view.

    Example 3:
    Input: heights = [1,3,2,4]
    Output: [3]
    Explanation: Only building 3 has an ocean view.
    """

    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        max_height = -inf
        for i in reversed(range(len(heights))):
            if max_height < heights[i]:
                ans.append(i)
                max_height = heights[i]
        ans.reverse()
        return ans


class _239:
    """
    # - Sliding Window Maximum -
    # https://leetcode.com/problems/sliding-window-maximum/
    """

    ...


class _212:
    """
    # - Word Search II -
    # https://leetcode.com/problems/word-search-ii/
    Given an m x n board of characters and a list of strings words, return all
    words on the board.

    Each word must be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring. The same
    letter cell may not be used more than once in a word.

    Example 1:
    Input: board = [["o","a","a","n"],
                    ["e","t","a","e"],
                    ["i","h","k","r"],
                    ["i","f","l","v"]],
    words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

    Example 2:
    Input: board = [["a","b"],
                    ["c","d"]],
    words = ["abcb"]
    Output: []
    """

    ...


class _704:
    """
    # - Binary Search -
    # https://leetcode.com/problems/binary-search/
    Given an array of integers nums which is sorted in ascending order, and an
    integer target, write a function to search target in nums. If target
    exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

    Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

    NOTE All the integers in nums are unique.
    """

    # This doesn't matter for Python, but when you do it in C++ it will:
    # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2
            if nums[pivot] == target:
                return pivot

            if target < nums[pivot]:
                r = pivot - 1
            else:
                l = pivot + 1
        return -1

    def search_(self, nums: List[int], target: int) -> int:
        index = bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


class _9:
    """
    # - Palindrome Number -
    # https://leetcode.com/problems/palindrome-number/
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.

    Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes
    121-. Therefore it is not a palindrome.

    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    """

    def isPalindrome(self, x: int) -> bool:
        """O(n) time, O(n) space"""
        return str(x) == str(x)[::-1]

    def isPalindrome_(self, x: int) -> bool:
        """O(log10(n)) time, O(1) space"""
        if x < 0 or (x % 10 == 0 and x != 0):  # negative number or trailing 0
            return False

        first_half, flipped_back_half = x, 0
        while first_half > flipped_back_half:
            flipped_back_half = flipped_back_half * 10 + first_half % 10
            first_half //= 10

        # ignore middle digit
        return first_half == flipped_back_half or first_half == flipped_back_half // 10


class _339:
    """
    # - Nested List Weight Sum -
    # https://leetcode.com/problems/nested-list-weight-sum/
    You are given a nested list of integers nestedList. Each element is either an
    integer or a list whose elements may also be integers or other lists.

    The depth of an integer is the number of lists that it is inside of. For example,
    the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

    Return the sum of each integer in nestedList multiplied by its depth.

    Example 1:
    nestedList = [[1, 1], 2, [1, 1]]
                  ______     ______
    depth      =   2  2       2  2
                  _________________
                          1

    Input: nestedList = [[1,1],2,[1,1]]
    Output: 10
    Explanation: Four 1's at depth 2, one 2 at depth 1.
    1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

    Example 2:
    Input: nestedList = [1,[4,[6]]]
    Output: 27
    Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3.
    1*1 + 4*2 + 6*3 = 27.

    Example 3:
    Input: nestedList = [0]
    Output: 0
    """

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)
        total, depth = 0, 1
        while queue:
            for _ in range(len(queue)):
                nested = queue.pop()
                if nested.isInteger():
                    total += nested.getInteger() * depth  # type: ignore
                else:
                    queue.extendleft(nested.getList())  # type: ignore
            depth += 1
        return total


class _1010:
    """
    # - Pairs of Songs With Total Durations Divisible by 60 -
    # https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
    """

    ...


class _696:
    """
    # - Count Binary Substrings -
    # https://leetcode.com/problems/count-binary-substrings/
    Give a binary string s, return the number of non-empty substrings that have
    the same number of 0's and 1's, and all the 0's and all the 1's in these
    substrings are grouped consecutively.

    Substrings that occur multiple times are counted the number of times they occur.

    Example 1:
    Input: s = "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's
    and 0's: "0011", "01", "1100", "10", "0011", and "01".
    Notice that some of these substrings repeat and are counted the number of
    times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are
    not grouped together.

    Example 2:
    Input: s = "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
    number of consecutive 1's and 0's.
    """

    def countBinarySubstrings(self, s: str) -> int:
        """O(n) time, O(n) space"""
        groups = [len(list(values)) for _, values in groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))

    def countBinarySubstrings_(self, s: str) -> int:
        """O(n) time, O(1) space"""
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cur += 1
            else:
                ans += min(prev, cur)
                prev, cur = cur, 1
        return ans + min(prev, cur)


class _17:
    """
    # - Letter Combinations of a Phone Number -
    # https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    """

    ...


class _54:
    """
    # - Spiral Matrix -
    # https://leetcode.com/problems/spiral-matrix/
    Given an m x n matrix, return all elements of the matrix in spiral order.

        Example 1:
        Input: [[ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ]]
        Output: [1,2,3,6,9,8,7,4,5]

        Example 2:
        Input: [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """

    ...


class _312:
    """
    # - Burst Balloons -
    # https://leetcode.com/problems/burst-balloons/
    """

    ...


class _13:
    """
    # - Roman to Integer -
    # https://leetcode.com/problems/roman-to-integer/
    """

    ...


class _938:
    """
    # - Range Sum of BST -
    # https://leetcode.com/problems/range-sum-of-bst/
    Given the root node of a binary search tree and two integers low and high,
    return the sum of values of all nodes with a value in the inclusive range
    [low, high].

    Example 1:
             10
       5           15
    3     7           18
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

    Example 2:
                         10
             5                       15
       3           7           13          18
    1           6
    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
    Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

    # NOTE All Node.val are unique.
    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        ans = 0
        dfs(root)
        return ans

    def rangeSumBST_(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        queue: Deque[Optional[TreeNode]] = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
        return ans


class _71:
    """
    # - Simplify Path -
    # https://leetcode.com/problems/simplify-path/
    Given a string path, which is an absolute path (starting with a slash '/') to a file
    or directory in a Unix-style file system, convert it to the simplified canonical
    path.

    In a Unix-style file system, a period '.' refers to the current directory, a double
    period '..' refers to the directory up a level, and any multiple consecutive slashes
    (i.e. '//') are treated as a single slash '/'. For this problem, any other format of
    periods such as '...' are treated as file/directory names.

    The canonical path should have the following format:
    * The path starts with a single slash '/'.
    * Any two directories are separated by a single slash '/'.
    * The path does not end with a trailing '/'.
    * The path only contains the directories on the path from the root directory to the
    target file or directory (i.e., no period '.' or double period '..')

    Return the simplified canonical path.

    Example 1:
    Input: path = "/home/"
    Output: "/home"
    Explanation: Note that there is no trailing slash after the last directory name.

    Example 2:
    Input: path = "/../"
    Output: "/"
    Explanation: Going one level up from the root directory is a no-op, as the root
    level is the highest level you can go.

    Example 3:
    Input: path = "/home//foo/"
    Output: "/home/foo"
    Explanation: In the canonical path, multiple consecutive slashes are replaced by a
    single one.

    NOTE path consists of English letters, digits, period '.', slash '/' or '_'.
    NOTE path is a valid absolute Unix path.
    """

    def simplifyPath(self, path: str) -> str:
        stack = []
        for x in path.split("/"):
            if x == "..":
                if stack:
                    stack.pop()
            elif x and x != ".":
                stack.append(x)
        return "/" + "/".join(stack)


class _217:
    """
    # - Contains Duplicate -
    # https://leetcode.com/problems/contains-duplicate/
    Given an integer array nums, return true if any value appears at least
    twice in the array, and return false if every element is distinct.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: true

    Example 2:
    Input: nums = [1,2,3,4]
    Output: false

    Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
    """

    ...


class _1650:
    """
    # - Lowest Common Ancestor of a Binary Tree III -
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
    """

    ...


class _224:
    """
    # - Basic Calculator -
    # https://leetcode.com/problems/basic-calculator/
    """

    ...


class _7:
    """
    # - Reverse Integer -
    # https://leetcode.com/problems/reverse-integer/
    Given a signed 32-bit integer x, return x with its digits reversed. If
    reversing x causes the value to go outside the signed 32-bit integer
    range [-231, 231 - 1], then return 0.

    Example 1:
    Input: x = 123
    Output: 321

    Example 2:
    Input: x = -123
    Output: -321

    Example 3:
    Input: x = 120
    Output: 21
    """

    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        reverse = int("".join(list(str(abs(x))[::-1])))
        if reverse > 2**31 - 1 or reverse < -1 * 2**31:
            return 0
        else:
            return sign * reverse


class _347:
    """
    # - Top K Frequent Elements -
    # https://leetcode.com/problems/top-k-frequent-elements/
    Given an integer array nums and an integer k, return the k most frequent
    elements. You may return the answer in any order.

    Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:
    Input: nums = [1], k = 1
    Output: [1]
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Bucket sort O(n) time, O(n) space"""
        bucket: List[List[int]] = [[] for _ in range(len(nums))]
        count = Counter(nums).items()
        for num, freq in count:
            bucket[freq - 1].append(num)
        return list(chain(*bucket))[::-1][:k]

    def topKFrequent_(self, nums: List[int], k: int) -> List[int]:
        """Heapq way, O(nlogn) or nlogk time, O(n) space"""
        count = Counter(nums)
        return nlargest(k, count.keys(), key=count.__getitem__)

    def topKFrequent__(self, nums: List[int], k: int) -> List[int]:
        """Calls heapq under the hood"""
        return [x for x, y in Counter(nums).most_common(k)]


class _443:
    """
    # - String Compression -
    # https://leetcode.com/problems/string-compression/
    Given an array of characters chars, compress it using the following algorithm:

    Begin with an empty string s. For each group of consecutive repeating
    characters in chars:
        - If the group's length is 1, append the character to s.
        - Otherwise, append the character followed by the group's length.

    The compressed string s should not be returned separately, but instead, be
    stored in the input character array chars. Note that group lengths that are
    10 or longer will be split into multiple characters in chars.

    After you are done modifying the input array, return the new length of the array.

    You must write an algorithm that uses only constant extra space.

    Example 1:
    Input: chars = ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input
    array should be: ["a","2","b","2","c","3"]
    Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

    Example 2:
    Input: chars = ["a"]
    Output: Return 1, and the first character of the input array should be: ["a"]
    Explanation: The only group is "a", which remains uncompressed since
    it's a single character.

    Example 3:
    Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output: Return 4, and the first 4 characters of the input array
    should be: ["a","b","1","2"].
    Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
    """

    def compress(self, chars: List[str]) -> int:
        """O(n) time, O(1) extra space"""
        slow = fast = 0
        while fast < len(chars):

            chars[slow] = chars[fast]
            count = 1

            while fast + 1 < len(chars) and chars[fast] == chars[fast + 1]:
                fast += 1
                count += 1

            if count > 1:
                for digit in str(count):
                    chars[slow + 1] = digit
                    slow += 1

            slow += 1
            fast += 1
        return slow


class _987:
    """
    # - Vertical Order Traversal of a Binary Tree -
    # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
    """

    ...


class _162:
    """
    # - Find Peak Element -
    # https://leetcode.com/problems/find-peak-element/
    """

    ...


class _829:
    """
    # - Consecutive Numbers Sum -
    # https://leetcode.com/problems/consecutive-numbers-sum/
    """

    ...


class _238:
    """
    # - Product of Array Except Self -
    # https://leetcode.com/problems/product-of-array-except-self/
    Given an integer array nums, return an array answer such that answer[i] is
    equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a
    32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the
    division operation.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    """

    ...


class _11:
    """
    # - Container With Most Water -
    # https://leetcode.com/problems/container-with-most-water/
    You are given an integer array height of length n. There are n vertical
    lines drawn such that the two endpoints of the ith line are (i, 0)
    and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that
    the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array
    [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section)
    the container can contain is 49.

    Example 2:
    Input: height = [1,1]
    Output: 1
    """

    ...


class _244:
    """
    # - Shortest Word Distance II -
    # https://leetcode.com/problems/shortest-word-distance-ii/
    """

    ...


class _48:
    """
    # - Rotate Image -
    # https://leetcode.com/problems/rotate-image/
    You are given an n x n 2D matrix representing an image, rotate the image by
    90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the
    input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

    Example 1:
    Input:
      [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
    Output:
      [[7, 4, 1],
       [8, 5, 2],
       [9, 6, 3]]

    Example 2:
    Input:
      [[ 5,  1,  9, 11],
       [ 2,  4,  8, 10],
       [13,  3,  6,  7],
       [15, 14, 12, 16]]
    Output:
      [[15, 13,  2,  5],
       [14,  3,  4,  1],
       [12,  6,  8,  9],
       [16,  7, 10, 11]]
    """

    # tuples accepted version
    # def rotate(self, matrix) -> None:
    # matrix[:] = list(zip(*matrix[::-1]))

    # peter norvig's transpose
    # >>> mat
    # [[1, 2], [3, 4]]
    # >>> list(zip(*mat))
    # [(1, 3), (2, 4)]

    # >>> def _(n):
    # ...     for i in range(n):
    # ...             for j in range(n//2):
    # ...                     print(i,j,-j-1)
    # ...
    # >>> _(5)
    # 0 0 -1
    # 0 1 -2
    # 1 0 -1
    # 1 1 -2
    # 2 0 -1
    # 2 1 -2
    # 3 0 -1
    # 3 1 -2
    # 4 0 -1
    # 4 1 -2

    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = list(list(row) for row in zip(*matrix[::-1]))

    class rotate_:
        # this is the "noooo stop being clever !!1" solution:
        def rotate(self, matrix: List[List[int]]) -> None:
            self.transpose(matrix)
            self.reflect(matrix)

        def transpose(self, matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        def reflect(self, matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


class _269:
    """
    # - Alien Dictionary -
    # https://leetcode.com/problems/alien-dictionary/
    There is a new alien language that uses the English alphabet. However, the
    order among the letters is unknown to you.

    You are given a list of strings words from the alien language's dictionary, where
    the strings in words are sorted lexicographically by the rules of this new language.

    Return a string of the unique letters in the new alien language sorted in
    lexicographically increasing order by the new language's rules. If there is no
    solution, return "". If there are multiple solutions, return any of them.

    A string `s` is lexicographically smaller than a string `t` if at the first letter where
    they differ, the letter in `s` comes before the letter in `t` in the alien language. If
    the first `min(s.length, t.length)` letters are the same, then `s` is smaller if and
    only if `s.length < t.length`.

    Example 1:
    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

    Example 2:
    Input: words = ["z","x"]
    Output: "zx"

    Example 3:
    Input: words = ["z","x","z"]
    Output: ""
    Explanation: The order is invalid, so return "".
    """

    ...


class _1268:
    """
    # - Search Suggestions System -
    # https://leetcode.com/problems/search-suggestions-system/
    """

    ...


class _210:
    """
    # - Course Schedule II -
    # https://leetcode.com/problems/course-schedule-ii/
    """

    ...


class _297:
    r"""
    # - Serialize and Deserialize Binary Tree -
    # https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
    Serialization is the process of converting a data structure or object into a
    sequence of bits so that it can be stored in a file or memory buffer, or
    transmitted across a network connection link to be reconstructed later in the
    same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no
    restriction on how your serialization/deserialization algorithm should work.
    You just need to ensure that a binary tree can be serialized to a string and
    this string can be deserialized to the original tree structure.

    Clarification: The input/output format is the same as how LeetCode serializes a
    binary tree. You do not necessarily need to follow this format, so please be
    creative and come up with different approaches yourself.

    Example 1:
        (1)
        / \
      (2) (3)
          / \
        (4) (5)
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

    Example 2:
    Input: root = []
    Output: []
    """
    ...


class _460:
    """
    # - LFU Cache -
    # https://leetcode.com/problems/lfu-cache/
    """

    ...


class _1041:
    """
    # - Robot Bounded In Circle -
    # https://leetcode.com/problems/robot-bounded-in-circle/
    """

    ...


class _759:
    """
    # - Employee Free Time -
    # https://leetcode.com/problems/employee-free-time/
    """

    ...


class _921:
    """
    # - Minimum Add to Make Parentheses Valid -
    # https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
    """

    ...


class _138:
    """
    # - Copy List with Random Pointer -
    # https://leetcode.com/problems/copy-list-with-random-pointer/
    """

    ...


class _1152:
    """
    # - Analyze User Website Visit Pattern -
    # https://leetcode.com/problems/analyze-user-website-visit-pattern/
    """

    ...


class _362:
    """
    # - Design Hit Counter -
    # https://leetcode.com/problems/design-hit-counter/
    """

    ...


class _1326:
    """
    # - Minimum Number of Taps to Open to Water a Garden -
    # https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
    """

    ...


class _981:
    """
    # - Time Based Key-Value Store -
    # https://leetcode.com/problems/time-based-key-value-store/
    """

    ...


class _366:
    """
    # - Find Leaves of Binary Tree -
    # https://leetcode.com/problems/find-leaves-of-binary-tree/
    Given the root of a binary tree, collect a tree's nodes as if you were doing this:

    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.

    Example 1:
             1
       2           3
    4     5
    Input: root = [1,2,3,4,5]
    Output: [[4,5,3],[2],[1]]
    Explanation:
    [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since
    per each level it does not matter the order on which elements are returned.

    Example 2:
    Input: root = [1]
    Output: [[1]]
    """

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """O(n) time and space"""

        def height(node):
            if not node:
                return 0
            h = 1 + max(height(node.left), height(node.right))
            seen[h].append(node.val)
            return h

        seen: Dict[int, List[int]] = defaultdict(list)
        height(root)
        return list(seen.values())


class _124:
    r"""
    # - Binary Tree Maximum Path Sum -
    # https://leetcode.com/problems/binary-tree-maximum-path-sum/
    A path in a binary tree is a sequence of nodes where each pair of adjacent
    nodes in the sequence has an edge connecting them. A node can only appear
    in the sequence at most once. Note that the path does not need to pass
    through the root.

    The path sum of a path is the sum of the node's values in the path.

    Given the root of a binary tree, return the maximum path sum of any non-empty path.

    Example 1:
        (1)
        / \
     (2)   (3)
    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
    # NOTE this is *not* a directed graph, you can go up the tree

    Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
    """
    ...


class _692:
    """
    # - Top K Frequent Words -
    # https://leetcode.com/problems/top-k-frequent-words/
    """

    ...


class _1197:
    """
    # - Minimum Knight Moves -
    # https://leetcode.com/problems/minimum-knight-moves/
    """

    ...


class _88:
    """
    # - Merge Sorted Array -
    # https://leetcode.com/problems/merge-sorted-array/
    """

    ...


class _529:
    """
    # - Minesweeper -
    # https://leetcode.com/problems/minesweeper/
    """

    ...


class _1507:
    """
    # - Reformat Date -
    # https://leetcode.com/problems/reformat-date/
    Given a date string in the form Day Month Year, where:

    Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
    Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
    "Aug", "Sep", "Oct", "Nov", "Dec"}.
    Year is in the range [1900, 2100].
    Convert the date string to the format YYYY-MM-DD, where:

    YYYY denotes the 4 digit year.
    MM denotes the 2 digit month.
    DD denotes the 2 digit day.

    Example 1:
    Input: date = "20th Oct 2052"
    Output: "2052-10-20"

    Example 2:
    Input: date = "6th Jun 1933"
    Output: "1933-06-06"

    Example 3:
    Input: date = "26th May 1960"
    Output: "1960-05-26"

    NOTE The given dates are guaranteed to be valid, so no error handling is necessary.
    """

    def reformatDate(self, date: str) -> str:
        months = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        d, m, y = date.split()
        return f"{y}-{(months.index(m)+1):02d}-{int(d[:-2]):02d}"


class _735:
    """
    # - Asteroid Collision -
    # https://leetcode.com/problems/asteroid-collision/
    """

    ...


class _295:
    """
    # - Find Median from Data Stream -
    # https://leetcode.com/problems/find-median-from-data-stream/
    The median is the middle value in an ordered integer list. If the size of the
    list is even, there is no middle value and the median is the mean of the two
    middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

    Implement the MedianFinder class:
    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the
    data structure.
    double findMedian() returns the median of all elements so far.
    Answers within 10-5
    of the actual answer will be accepted.

    Example 1:
    Input
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
    Output
    [null, null, null, 1.5, null, 2.0]

    Explanation
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0
    """

    ...


class _10:
    """
    # - Regular Expression Matching -
    # https://leetcode.com/problems/regular-expression-matching/
    """

    ...


class _875:
    """
    # - Koko Eating Bananas -
    # https://leetcode.com/problems/koko-eating-bananas/
    """

    ...


class _364:
    """
    # - Nested List Weight Sum II -
    # https://leetcode.com/problems/nested-list-weight-sum-ii/
    """

    ...


class _199:
    """
    # - Binary Tree Right Side View -
    # https://leetcode.com/problems/binary-tree-right-side-view/
    """

    ...


class _1293:
    """
    # - Shortest Path in a Grid with Obstacles Elimination -
    # https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
    """

    ...


class _139:
    """
    # - Word Break -
    # https://leetcode.com/problems/word-break/
    """

    ...


class _84:
    """
    # - Largest Rectangle in Histogram -
    # https://leetcode.com/problems/largest-rectangle-in-histogram/
    """

    ...


class _937:
    """
    # - Reorder Data in Log Files -
    #
    """

    ...


class _125:
    """
    # - Valid Palindrome -
    # https://leetcode.com/problems/valid-palindrome/
    A phrase is a palindrome if, after converting all uppercase letters into
    lowercase letters and removing all non-alphanumeric characters, it reads the
    same forward and backward. Alphanumeric characters include letters and
    numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric
    characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
    """

    ...


class _12:
    """
    # - Integer to Roman -
    # https://leetcode.com/problems/integer-to-roman/
    """

    ...


class _198:
    """
    # - House Robber -
    # https://leetcode.com/problems/house-robber/
    You are a professional robber planning to rob houses along a street. Each
    house has a certain amount of money stashed, the only constraint stopping
    you from robbing each of them is that adjacent houses have security system
    connected and it will automatically contact the police if two adjacent
    houses were broken into on the same night. Given a list of non-negative
    integers representing the amount of money of each house, determine the
    maximum amount of money you can rob tonight without alerting the police.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house
    5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12."""

    ...


class _926:
    """
    # - Flip String to Monotone Increasing -
    # https://leetcode.com/problems/flip-string-to-monotone-increasing/
    """

    ...


class _716:
    """
    # - Max Stack -
    # https://leetcode.com/problems/max-stack/
    Design a max stack data structure that supports the stack operations and
    supports finding the stack's maximum element.

    Implement the MaxStack class:
    * MaxStack() Initializes the stack object.
    * void push(int x) Pushes element x onto the stack.
    * int pop() Removes the element on top of the stack and returns it.
    * int top() Gets the element on the top of the stack without removing it.
    * int peekMax() Retrieves the maximum element in the stack without removing it.
    * int popMax() Retrieves the maximum element in the stack and removes it. If
    there is more than one maximum element, only remove the top-most one.

    Example 1:
    Input:
    ["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]
    [[]        , [5]  , [1]  , [5]  , []  , []     , []  , []      , []  , []]
    Output:
    [null      , null , null , null , 5   , 5      , 1   , 5       , 1   , 5]
    Explanation
    MaxStack stk = new MaxStack();
    stk.push(5);   // [5] the top of the stack and the maximum number is 5.
    stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
    stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the
                      maximum, because it is the top most one.
    stk.top();     // return 5, [5, 1, 5] the stack did not change.
    stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is
                      different from the max.
    stk.top();     // return 1, [5, 1] the stack did not change.
    stk.peekMax(); // return 5, [5, 1] the stack did not change.
    stk.pop();     // return 1, [5] the top of the stack and the max element is
                      now 5.
    stk.top();     // return 5, [5] the stack did not change.

    Constraints:
    NOTE There will be at least one element in the stack when pop, top, peekMax, or
    popMax is called.
    """

    class MaxStack(list):
        """O(n) time popmax, O(1) time others, O(n) space"""

        def push(self, x):
            mx = max(x, self[-1][1] if self else -inf)
            self.append((x, mx))

        def pop(self):
            return list.pop(self)[0]  # self.pop()[0]

        def top(self):
            return self[-1][0]

        def peekMax(self):
            return self[-1][1]

        def popMax(self):
            mx = self[-1][1]
            b = []
            while self[-1][0] != mx:
                b.append(self.pop())

            self.pop()
            for item in reversed(b):
                self.push(item)
            return mx

    # TODO this passses leetcode but doesn't typecheck need to fix
    #      and isnt popmax/peepmax nlogn?
    # class MaxStack_:
    #     """O(logn) time popmax, O(1) time others, O(n) space"""
    #     def __init__(self) -> None:
    #         self.key = 0
    #         self.heap = []
    #         self.od = OrderedDict()

    #     def push(self, x: int) -> None:
    #         heappush(self.heap, (-x, self.key))
    #         self.od[self.key] = x
    #         self.key -= 1

    #     def pop(self) -> int:
    #         k, x = self.od.popitem(last=True)
    #         return x

    #     def top(self) -> int:
    #         key, x = self.od.popitem(last=True)
    #         self.od[key] = x
    #         return x

    #     def peekMax(self) -> int:
    #         while self.heap:
    #             x, key = heappop(self.heap)
    #             if key in self.od:
    #                 break
    #         heappush(self.heap, (x, key))
    #         return -x

    #     def popMax(self) -> int:
    #         while self.heap:
    #             x, key = heappop(self.heap)
    #             if key in self.od:
    #                 break
    #         self.od.pop(key)
    #         return -x


class _453:
    """
    # - Minimum Moves to Equal Array Elements -
    # https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
    """

    ...


class _51:
    """
    # - N-Queens -
    # https://leetcode.com/problems/n-queens/
    """

    ...


class _1604:
    """
    # - Alert Using Same Key-Card Three or More Times in a One Hour Period -
    # https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
    """

    ...


class _387:
    """
    # - First Unique Character in a String -
    # https://leetcode.com/problems/first-unique-character-in-a-string/
    Given a string s, find the first non-repeating character in it and return
    its index. If it does not exist, return -1.

    Example 1:
    Input: s = "leetcode"
    Output: 0

    Example 2:
    Input: s = "loveleetcode"
    Output: 2

    Example 3:
    Input: s = "aabb"
    Output: -1
    """

    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1


class _863:
    """
    # - All Nodes Distance K in Binary Tree -
    # https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
    """

    ...


class _55:
    """
    # - Jump Game -
    # https://leetcode.com/problems/jump-game/
    You are given an integer array nums. You are initially positioned at the array's
    first index, and each element in the array represents your maximum jump length at
    that position.

    Return true if you can reach the last index, or false otherwise.

    Example 1:

    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    Example 2:

    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump
    length is 0, which makes it impossible to reach the last index."""

    ...


class _221:
    """
    # - Maximal Square -
    # https://leetcode.com/problems/maximal-square/
    """

    ...


class _1048:
    """
    # - Longest String Chain -
    # https://leetcode.com/problems/longest-string-chain/
    """

    ...


class _45:
    """
    # - Jump Game II -
    # https://leetcode.com/problems/jump-game-ii/
    """

    ...


class _70:
    """
    # - Climbing Stairs -
    # https://leetcode.com/problems/climbing-stairs/
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can
    you climb to the top?

    Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

    Constraints:
    1 <= n <= 45"""

    ...


class _415:
    """
    # - Add Strings -
    # https://leetcode.com/problems/add-strings/
    Given two non-negative integers, num1 and num2 represented as string,
    return the sum of num1 and num2 as a string.

    You must solve the problem without using any built-in library for
    handling large integers (such as BigInteger). You must also not convert
    the inputs to integers directly.

    Example 1:
    Input: num1 = "11", num2 = "123"
    Output: "134"

    Example 2:
    Input: num1 = "456", num2 = "77"
    Output: "533"

    Example 3:
    Input: num1 = "0", num2 = "0"
    Output: "0"
    """

    def addStrings(self, num1: str, num2: str) -> str:
        ans: List[int] = []
        quotient = 0
        for x, y in zip_longest(reversed(num1), reversed(num2), fillvalue="0"):
            quotient, remainder = divmod(quotient + int(x) + int(y), 10)
            ans.append(remainder)
        if quotient:
            ans.append(quotient)
        return "".join(map(str, reversed(ans)))


class _1209:
    """
    # - Remove All Adjacent Duplicates in String II -
    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
    """

    ...


class _994:
    """
    # - Rotting Oranges -
    # https://leetcode.com/problems/rotting-oranges/
    """

    ...


class _34:
    """
    # - Find First and Last Position of Element in Sorted Array -
    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    """

    ...


class _174:
    """
    # - Dungeon Game -
    # https://leetcode.com/problems/dungeon-game/
    """

    ...


class _721:
    """
    # - Accounts Merge -
    # https://leetcode.com/problems/accounts-merge/
    """

    ...


class _1044:
    """
    # - Longest Duplicate Substring -
    # https://leetcode.com/problems/longest-duplicate-substring/
    """

    ...


class _509:
    """
    # - Fibonacci Number -
    # https://leetcode.com/problems/fibonacci-number/
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
    Fibonacci sequence, such that each number is the sum of the two preceding
    ones, starting from 0 and 1. That is,

    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).

    Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

    Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
    """

    def fib(self, N: int) -> int:
        """O(logn) time O(1) space"""
        golden_ratio = (1 + (5**0.5)) / 2
        return round((golden_ratio**N) / (5**0.5))

    def fib_(self, N: int) -> int:
        """O(n) time, O(1) space"""
        if N <= 1:
            return N
        a, b = 0, 1
        for _ in range(2, N + 1):
            a, b = b, a + b
        return b


class _140:
    """
    # - Word Break II -
    # https://leetcode.com/problems/word-break-ii/
    """

    ...


class _399:
    """
    # - Evaluate Division -
    # https://leetcode.com/problems/evaluate-division/
    """

    ...


class _739:
    """
    # - Daily Temperatures -
    # https://leetcode.com/problems/daily-temperatures/
    """

    ...


class _426:
    """
    # - Convert Binary Search Tree to Sorted Doubly Linked List -
    # https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
    """

    ...


class _697:
    """
    # - Degree of an Array -
    # https://leetcode.com/problems/degree-of-an-array/
    Given a non-empty array of non-negative integers nums, the degree of this array
    is defined as the maximum frequency of any one of its elements.

    Your task is to find the smallest possible length of a (contiguous) subarray of
    nums, that has the same degree as nums.

    Example 1:
    Input: nums = [1,2,2,3,1]
    Output: 2
    Explanation:
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.

    Example 2:
    Input: nums = [1,2,2,3,1,4,2]
    Output: 6
    Explanation:
    The degree is 3 because the element 2 is repeated 3 times.
    So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
    """

    def findShortestSubArray(self, nums: List[int]) -> int:
        """O(n) time and space"""
        left: Dict[int, int] = {}
        right: Dict[int, int] = {}
        count: Dict[int, int] = {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans


class _18:
    """
    # - 4Sum -
    #
    """

    ...


class _695:
    """
    # - Max Area of Island -
    # https://leetcode.com/problems/flood-fill/
    """

    ...


class _543:
    """
    # - Diameter of Binary Tree -
    # https://leetcode.com/problems/diameter-of-binary-tree/
    Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any
    two nodes in a tree. This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges
    between them.

    Example 1:
             1
       2           3
    4     5
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

    Example 2:
    Input: root = [1,2]
    Output: 1
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """O(n) time and space"""

        def dfs(node):
            if not node:
                return 0
            nonlocal ans
            path_l, path_r = dfs(node.left), dfs(node.right)
            ans = max(ans, path_l + path_r)
            return max(path_l, path_r) + 1

        ans = 0
        dfs(root)
        return ans

    def diameterOfBinaryTree_(self, root: Optional[TreeNode]) -> int:
        """O(n) time and space"""

        def dfs(node):
            if not node:
                return (0, 0)
            path_l, ans_l = dfs(node.left)
            path_r, ans_r = dfs(node.right)
            return max(path_l, path_r) + 1, max(ans_l, ans_r, path_l + path_r)

        return dfs(root)[1]


class _151:
    """
    # - Reverse Words in a String -
    # https://leetcode.com/problems/reverse-words-in-a-string/
    """

    ...


class _605:
    """
    # - Can Place Flowers -
    # https://leetcode.com/problems/can-place-flowers/
    You have a long flowerbed in which some of the plots are planted, and some
    are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and
    1 means not empty, and an integer n, return if n new flowers can be planted in
    the flowerbed without violating the no-adjacent-flowers rule.

    Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

    Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

    NOTE There are no two adjacent flowers in flowerbed.
    """

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """O(n) time O(1) space"""
        for i, x in enumerate(flowerbed):
            if (
                x == 0
                and (i == 0 or flowerbed[i - 1] == 0)  # empty left
                and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0)  # empty right
            ):
                n -= 1
                flowerbed[i] = 1
                if n <= 0:
                    return True
        return n <= 0


class _525:
    """
    # - Contiguous Array -
    # https://leetcode.com/problems/contiguous-array/
    """

    ...


class _1094:
    """
    # - Car Pooling -
    # https://leetcode.com/problems/car-pooling/
    """

    ...


class _317:
    """
    # - Shortest Distance from All Buildings -
    # https://leetcode.com/problems/shortest-distance-from-all-buildings/
    """

    ...


class _1207:
    """
    # - Unique Number of Occurrences -
    # https://leetcode.com/problems/unique-number-of-occurrences/
    Given an array of integers arr, return true if the number of occurrences of
    each value in the array is unique, or false otherwise.

    Example 1:
    Input: arr = [1,2,2,1,1,3]
    Output: true
    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
    values have the same number of occurrences.

    Example 2:
    Input: arr = [1,2]
    Output: false

    Example 3:
    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """O(n) time and space"""
        freq = Counter(arr)
        return len(freq) == len(set(freq.values()))


class _25:
    """
    # - Reverse Nodes in k-Group -
    # https://leetcode.com/problems/reverse-nodes-in-k-group/
    """

    ...


class _408:
    """
    # - Valid Word Abbreviation -
    # https://leetcode.com/problems/valid-word-abbreviation/
    A string can be abbreviated by replacing any number of non-adjacent, non-empty
    substrings with their lengths. The lengths should not have leading zeros.

    For example, a string such as "substitution" could be abbreviated as (but not
    limited to):
        "s10n" ("s ubstitutio n")
        "sub4u4" ("sub stit u tion")
        "12" ("substitution")
        "su3i1u2on" ("su bst i t u ti on")
        "substitution" (no substrings replaced)

    The following are not valid abbreviations:
        "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
        "s010n" (has leading zeros)
        "s0ubstitution" (replaces an empty substring)

    Given a string word and an abbreviation abbr, return whether the string
    matches the given abbreviation.

    A substring is a contiguous non-empty sequence of characters within a string.

    Example 1:
    Input: word = "internationalization", abbr = "i12iz4n"
    Output: true
    Explanation: The word "internationalization" can be abbreviated as "i12iz4n"
    ("i nternational iz atio n").

    Example 2:
    Input: word = "apple", abbr = "a2e"
    Output: false
    Explanation: The word "apple" cannot be abbreviated as "a2e".
    """

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """O(n) time, O(1) space"""
        i = num = 0
        for j, char in enumerate(abbr):
            if char.isdigit():
                if num == 0 and char == "0":
                    return False
                num = int(char) + 10 * num
            else:
                i, num = i + num, 0
                if i >= len(word) or word[i] != char:
                    return False
                i += 1
        return (i + num) == len(word)


class _322:
    """
    # - Coin Change -
    # https://leetcode.com/problems/coin-change/
    You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If
    that amount of money cannot be made up by any combination of the coins,
    return -1.

    You may assume that you have an infinite number of each kind of coin.

    Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

    Example 2:
    Input: coins = [2], amount = 3
    Output: -1

    Example 3:
    Input: coins = [1], amount = 0
    Output: 0

    Constraints:

    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104"""

    ...


class _540:
    """
    # - Single Element in a Sorted Array -
    # https://leetcode.com/problems/dsingle-element-in-a-sorted-array/
    """

    ...


class _1761:
    """
    # - Minimum Degree of a Connected Trio in a Graph -
    # https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
    """

    ...


class _1487:
    """
    # - Making File Names Unique -
    # https://leetcode.com/problems/making-file-names-unique/
    """

    ...


class _871:
    """
    # - Minimum Number of Refueling Stops -
    # https://leetcode.com/problems/minimum-number-of-refueling-stops/
    """

    ...


class _412:
    """
    # - Fizz Buzz -
    # https://leetcode.com/problems/fizz-buzz/
    Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

    Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]

    Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

    Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz",
    "13","14","FizzBuzz"]
    """

    def fizzBuzz(self, n: int) -> List[str]:
        """O(n) time, O(1) space"""
        ans: List[str] = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans


class _767:
    """
    # - Reorganize String -
    # https://leetcode.com/problems/reorganize-string/
    """

    ...


class _636:
    """
    # - Exclusive Time of Functions -
    # https://leetcode.com/problems/exclusive-time-of-functions/
    """

    ...


class _370:
    """
    # - Range Addition -
    # https://leetcode.com/problems/range-addition/
    """

    ...


class _207:
    """
    # - Course Schedule -
    # https://leetcode.com/problems/course-schedule/
    There are a total of numCourses courses you have to take, labeled from 0
    to numCourses - 1. You are given an array prerequisites where
    prerequisites[i] = [ai, bi] indicates that you must take course bi first
    if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to
    first take course 1. Return true if you can finish all courses.
    Otherwise, return false.

    Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

    Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

    # NOTE All the pairs prerequisites[i] are unique.
    """

    ...


class _76:
    """
    # - Minimum Window Substring -
    # https://leetcode.com/problems/minimum-window-substring/
    Given two strings s and t of lengths m and n respectively, return the minimum
    window substring of s such that every character in t (including duplicates)
    is included in the window. If there is no such substring, return the empty
    string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.

    Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

    Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

    Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.
    """

    ...


class _74:
    """
    # - Search a 2D Matrix -
    # https://leetcode.com/problems/search-a-2d-matrix/
    """

    ...


class _1091:
    """
    # - Shortest Path in Binary Matrix -
    # https://leetcode.com/problems/shortest-path-in-binary-matrix/
    Given an n x n binary matrix grid, return the length of the shortest clear
    path in the matrix. If there is no clear path, return -1.

    A clear path in a binary matrix is a path from the top-left cell (i.e.,
    (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e.,
    they are different and they share an edge or a corner).
    The length of a clear path is the number of visited cells of this path.

    Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: 2

    Example 2:
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

    Example 3:
    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """O(n) time O(n) space, BFS"""
        m = len(grid)  # NOTE n == m
        if grid[0][0] or grid[m - 1][m - 1]:
            return -1
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]
        seen = set()
        queue: Deque[tuple[int, int, int]] = deque([(0, 0, 1)])  # (x, y, dist)
        seen.add((0, 0))
        while queue:
            i, j, dist = queue.popleft()
            if i == m - 1 and j == m - 1:
                return dist
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < m and (x, y) not in seen and grid[x][y] == 0:
                    seen.add((x, y))
                    queue.append((x, y, dist + 1))
        return -1

    # NOTE A* solution exists


class _37:
    """
    # - Sudoku Solver -
    # https://leetcode.com/problems/sudoku-solver/
    """

    ...


class _21:
    """
    # - Merge Two Sorted Lists -
    # https://leetcode.com/problems/merge-two-sorted-lists/
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing
    together the nodes of the first two lists.

    Return the head of the merged linked list.

    Example 1:
    (1) -> (2) -> (4)
    (1) -> (3) -> (4)

            |
            v

    (1) -> (1) -> (2) -> (3) -> (4) -> (4)

    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example 2:

    Input: list1 = [], list2 = []
    Output: []

    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]
    """

    ...


class _234:
    """
    # - Palindrome Linked List -
    # https://leetcode.com/problems/palindrome-linked-list/
    Given the head of a singly linked list, return true if it is a palindrome.

    Example 1:
    1->2->2->1
    Input: head = [1,2,2,1]
    Output: true

    Example 2:
    1->2
    Input: head = [1,2]
    Output: false

    NOTE 0 <= Node.val <= 9
    """

    # NOTE only use node.val and node.next of ListNode

    def isPalindrome(self, head):
        """Maintain list method: O(n) time O(1) space"""
        if head is None:
            return False

        def middleNode(head):
            # in a->b->c->d, want b
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverseList(head):
            prev, curr = None, head
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev

        mid = middleNode(head)
        tail = reverseList(mid.next)  # reverse second half
        _head, _tail = head, tail
        ans = True
        while ans and _tail is not None:
            if _head.val != _tail.val:
                ans = False  # don't early out so we can restore list
            _head = _head.next
            _tail = _tail.next
        mid.next = reverseList(tail)  # restore list
        return ans

    # def isPalindrome_(self, head: Optional[ListNode]) -> bool:
    #     """Destroy list method: O(n) time O(1) space"""
    #     fast = slow = head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next

    #     prev = None
    #     while slow:
    #         slow.next, slow, prev = prev, slow.next, slow

    #     while prev and head.val == prev.val:
    #         head = head.next
    #         prev = prev.next

    #     return not prev


class _289:
    """
    # - Game of Life -
    # https://leetcode.com/problems/game-of-life/
    According to Wikipedia's article: "The Game of Life, also known simply as
    Life, is a cellular automaton devised by the British mathematician John
    Horton Conway in 1970."

    The board is made up of an m x n grid of cells, where each cell has an initial
    state: live (represented by a 1) or dead (represented by a 0). Each cell
    interacts with its eight neighbors (horizontal, vertical, diagonal) using the
    following four rules (taken from the above Wikipedia article):
        - Any live cell with fewer than two live neighbors dies as if caused by
        under-population.
        - Any live cell with two or three live neighbors lives on to the next
        generation.
        - Any live cell with more than three live neighbors dies, as if by
        over-population.
        - Any dead cell with exactly three live neighbors becomes a live cell,
        as if by reproduction.

    The next state is created by applying the above rules simultaneously to ever
    cell in the current state, where births and deaths occur simultaneously.
    Given the current state of the m x n grid board, return the next state.

    Example 1:
    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    Example 2:
    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]
    """

    def gameOfLife(self, board: List[List[int]]) -> None:
        """O(mn) time and space"""
        m, n = len(board), len(board[0])
        alive = set(
            [(i, j) for i, j in product(range(m), range(n)) if board[i][j] == 1]
        )
        neighbors = list(product(range(-1, 2), range(-1, 2)))

        count = Counter()

        for i, j in alive:
            for dx, dy in neighbors:
                count[(i + dx, j + dy)] += 1

        for x, y in count:
            if 0 <= x < m and 0 <= y < n:
                if count[x, y] == 3 and board[x][y] == 0:
                    board[x][y] = 1
                if count[x, y] not in [3, 4]:  # [2, 3], but count includes itself
                    board[x][y] = 0


class _1146:
    """
    # - Snapshot Array -
    # https://leetcode.com/problems/snapshot-array/
    """

    ...


class _1291:
    """
    # - Sequential Digits -
    # https://leetcode.com/problems/sequential-digits/
    """

    ...


class _442:
    """
    # - Find All Duplicates in an Array -
    # https://leetcode.com/problems/find-all-duplicates-in-an-array/
    """

    ...


class _32:
    """
    # - Longest Valid Parentheses -
    # https://leetcode.com/problems/longest-valid-parentheses/
    """

    ...


class _790:
    """
    # - Domino and Tromino Tiling -
    # https://leetcode.com/problems/domino-and-tromino-tiling/
    """

    ...


class _465:
    """
    # - Optimal Account Balancing -
    # https://leetcode.com/problems/optimal-account-balancing/
    """

    ...


class _65:
    """
    # - Valid Number -
    # https://leetcode.com/problems/valid-number/
    """

    ...


class _438:
    """
    # - Find All Anagrams in a String -
    # https://leetcode.com/problems/find-all-anagrams-in-a-string/
    """

    ...


class _723:
    """
    # - Candy Crush -
    # https://leetcode.com/problems/candy-crush/
    """

    ...


class _670:
    """
    # - Maximum Swap -
    # https://leetcode.com/problems/maximum-swap/
    """

    ...


class _878:
    """
    # - Nth Magical Number -
    # https://leetcode.com/problems/nth-magical-number/
    """

    ...


class _909:
    """
    # - Snakes and Ladders -
    # https://leetcode.com/problems/snakes-and-ladders/
    """

    ...


class _410:
    """
    # - Split Array Largest Sum -
    # https://leetcode.com/problems/split-array-largest-sum/
    """

    ...


class _421:
    """
    # - Maximum XOR of Two Numbers in an Array -
    # https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
    """

    ...


class _16:
    """
    # - 3Sum Closest -
    #
    """

    ...


class _1011:
    """
    # - Capacity To Ship Packages Within D Days -
    # https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
    """

    ...


class _827:
    """
    # - Making A Large Island -
    # https://leetcode.com/problems/making-a-large-island/
    """

    ...


class _556:
    """
    # - Next Greater Element III -
    # https://leetcode.com/problems/next-greater-element-iii/
    """

    ...


class _1472:
    """
    # - Design Browser History -
    # https://leetcode.com/problems/design-browser-history/
    """

    ...


class _278:
    """
    # - First Bad Version -
    # https://leetcode.com/problems/first-bad-version/
    You are a product manager and currently leading a team to develop a new product.
    Unfortunately, the latest version of your product fails the quality check.
    Since each version is developed based on the previous version, all the versions
    after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad
    one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether version is bad.
    Implement a function to find the first bad version. You should minimize the number of
    calls to the API.

    Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

    Example 2:
    Input: n = 1, bad = 1
    Output: 1

    NOTE The isBadVersion API is already defined for you:
    """

    def firstBadVersion(self, n: int) -> int:
        """O(logn) time O(1) space"""
        # NOTE see search(...) for an alternate binary search implementation
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


class _420:
    """
    # - Strong Password Checker -
    # https://leetcode.com/problems/strong-password-checker/
    """

    ...


class _1710:
    """
    # - Maximum Units on a Truck -
    # https://leetcode.com/problems/maximum-units-on-a-truck/
    You are assigned to put some amount of boxes onto one truck. You are given a 2D
    array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
    * numberOfBoxesi is the number of boxes of type i.
    * numberOfUnitsPerBoxi is the number of units in each box of the type i.

    You are also given an integer truckSize, which is the maximum number of boxes
    that can be put on the truck. You can choose any boxes to put on the truck as
    long as the number of boxes does not exceed truckSize.

    Return the maximum total number of units that can be put on the truck.

    Example 1:
    Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
    Output: 8
    Explanation: There are:
    - 1 box of the first type that contains 3 units.
    - 2 boxes of the second type that contain 2 units each.
    - 3 boxes of the third type that contain 1 unit each.
    You can take all the boxes of the first and second types, and one box of
    the third type.
    The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

    Example 2:
    Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
    Output: 91
    """

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """O(nlogn) time O(n) space"""
        ans = 0
        for boxes, units in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            boxes = min(boxes, truckSize)
            ans += boxes * units
            truckSize -= boxes
        return ans


class _150:
    """
    # - Evaluate Reverse Polish Notation -
    # https://leetcode.com/problems/evaluate-reverse-polish-notation/
    """

    ...


class _332:
    """
    # - Reconstruct Itinerary -
    # https://leetcode.com/problems/reconstruct-itinerary/
    """

    ...


class _498:
    """
    # - Diagonal Traverse -
    # https://leetcode.com/problems/diagonal-traverse/
    """

    ...


class _36:
    """
    # - Valid Sudoku -
    # https://leetcode.com/problems/valid-sudoku/
    """

    ...


class _679:
    """
    # - 24 Game -
    # https://leetcode.com/problems/24-game/
    """

    ...


class _780:
    """
    # - Reaching Points -
    # https://leetcode.com/problems/reaching-points/
    """

    ...


class _329:
    """
    # - Longest Increasing Path in a Matrix -
    # https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
    """

    ...


class _103:
    """
    # - Binary Tree Zigzag Level Order Traversal -
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    """

    ...


class _62:
    """
    # - Unique Paths -
    # https://leetcode.com/problems/unique-paths/
    There is a robot on an m x n grid. The robot is initially located at the top-left
    corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
    (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any
    point in time.

    Given the two integers m and n, return the number of possible unique paths that the
    robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or equal to 2*109.

    Example 1:
    R ??? ??? ??? ??? ??? ???
    ??? ??? ??? ??? ??? ??? ???
    ??? ??? ??? ??? ??? ??? S
    Input: m = 3, n = 7
    Output: 28

    Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the
    bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down"""

    ...


class _718:
    """
    # - Maximum Length of Repeated Subarray -
    # https://leetcode.com/problems/maximum-length-of-repeated-subarray/
    """

    ...


class _46:
    """
    # - Permutations -
    # https://leetcode.com/problems/permutations/
    Given an array nums of distinct integers, return all the possible
    permutations. You can return the answer in any order.

    Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

    Example 3:
    Input: nums = [1]
    Output: [[1]]

    NOTE All the integers of nums are unique.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                ans.append(nums[:])  # NOTE you want to copy the array with [:]
                # otherwise it's object references
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  # backtrack

        n = len(nums)
        ans = []
        backtrack()
        return ans


class _1861:
    """
    # - Rotating the Box -
    # https://leetcode.com/problems/rotating-the-box/
    """

    ...


class _849:
    """
    # - Maximize Distance to Closest Person -
    # https://leetcode.com/problems/maximize-distance-to-closest-person/
    """

    ...


class _532:
    """
    # - K-diff Pairs in an Array -
    # https://leetcode.com/problems/k-diff-pairs-in-an-array/
    """

    ...


class _287:
    """
    # - Find the Duplicate Number -
    # https://leetcode.com/problems/find-the-duplicate-number/
    """

    ...


class _44:
    """
    # - Wildcard Matching -
    # https://leetcode.com/problems/wildcard-matching/
    """

    ...


class _916:
    """
    # - 916. Word Subsets -
    # https://leetcode.com/problems/word-subsets/
    You are given two string arrays words1 and words2.

    A string b is a subset of string a if every letter in b occurs in a
    including multiplicity.

    For example, "wrr" is a subset of "warrior" but is not a subset of "world".
    A string a from words1 is universal if for every string b in words2, b is
    a subset of a.

    Return an array of all the universal strings in words1. You may return the
    answer in any order.

    Example 1:
    Input: words1 = ["amazon","apple","facebook","google","leetcode"],
    words2 = ["e","o"]
    Output: ["facebook","google","leetcode"]
    Example 2:

    Input: words1 = ["amazon","apple","facebook","google","leetcode"],
    words2 = ["l","e"]
    Output: ["apple","google","leetcode"]
    NOTE words1[i] and words2[i] consist only of lowercase English letters.
    NOTE All the strings of words1 are unique.
    """

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for word in words2:
            count |= Counter(word)
        return [word for word in words1 if not count - Counter(word)]

    # NOTE this solution abuses that Counters dont store negatives
    # >>> a
    # Counter({'a': 2, 'b': 1})
    # >>> b
    # Counter({'a': 1, 'b': 1})
    # >>> a - b
    # Counter({'a': 1})
    # >>> b - a
    # Counter()


class _169:
    """
    # - Majority Element -
    # https://leetcode.com/problems/majority-element/
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ???n / 2??? times.
    You may assume that the majority element always exists in the array.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    """

    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore method: O(n) time O(1) space"""
        ans = vote = 0
        for x in nums:
            if vote == 0:
                ans = x
            if x == ans:
                vote += 1
            else:
                vote -= 1
        return ans

    def majorityElement_(self, nums: List[int]) -> int:
        """Dictionary method: O(n) time O(n) space"""
        counts: Dict[int, int] = {}  # {num:count}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num
        raise RuntimeError("Couldn't find majority element in array.")


class _359:
    """
    # - Logger Rate Limiter -
    # https://leetcode.com/problems/logger-rate-limiter/
    Design a logger system that receives a stream of messages along with their
    timestamps. Each unique message should only be printed at most every 10 seconds
    (i.e. a message printed at timestamp t will prevent other identical messages
    from being printed until timestamp t + 10). All messages will come in
    chronological order. Several messages may arrive at the same timestamp.

    Implement the Logger class:
    * Logger() Initializes the logger object.
    * bool shouldPrintMessage(int timestamp, string message) Returns true if the
    message should be printed in the given timestamp, otherwise returns false.

    Example 1:
    Input: ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
    "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
    [[], [1, "foo"], [2, "bar"], [3, "foo"],
    [8, "bar"], [10, "foo"], [11, "foo"]]
    Output: [null, true, true, false, false, false, true]
    Explanation:
    Logger logger = new Logger();
    logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for
                                          // "foo" is 1 + 10 = 11
    logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for
                                          // "bar" is 2 + 10 = 12
    logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
    logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
    logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
    logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed
                                          // timestamp for "foo" is 11 + 10 = 21

    NOTE Every timestamp will be passed in non-decreasing order (chronological order).
    """

    class Logger:
        """O(1) time O(n) space"""

        def __init__(self):
            self.seen: Dict[str, int] = {}

        def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
            if timestamp - self.seen.get(message, -inf) >= 10:
                self.seen[message] = timestamp
                return True
            return False


class _189:
    """
    # - Rotate Array -
    # https://leetcode.com/problems/rotate-array/
    """

    ...


class _706:
    """
    # - Design HashMap -
    # https://leetcode.com/problems/design-hashmap/
    Design a HashMap without using any built-in hash table libraries.

    Implement the MyHashMap class:
    * MyHashMap() initializes the object with an empty map.
    * void put(int key, int value) inserts a (key, value) pair into the HashMap.
    If the key already exists in the map, update the corresponding value.
    * int get(int key) returns the value to which the specified key is mapped,
    or -1 if this map contains no mapping for the key.
    * void remove(key) removes the key and its corresponding value if the map
    contains the mapping for the key.

    Example 1:
    Input
    ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    Output
    [null, null, null, 1, -1, null, 1, null, -1]

    Explanation
    MyHashMap myHashMap = new MyHashMap();
    myHashMap.put(1, 1); // The map is now [[1,1]]
    myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
    myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
    myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
    myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (update the existing value)
    myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
    myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
    myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

    NOTE 0 <= key, value <= 106
    """

    # this question is too open ended, don't think too hard about it

    class MyHashMap:
        w: Final = 32
        k: Final = 10
        M: Final = 2**k
        W: Final = 2**w
        a: Final = round(2 / (1 + (5 ** (1 / 2))) * W)

        def __init__(self) -> None:
            # NOTE this doesn't implement rehashing, it's a fixed size hashmap
            self.arr = [[] for _ in range(self.M)]

        def _hash(self, key: int) -> int:
            # fibonnaci hashing, good for the low number range given
            return ((self.a * key) & (self.W - 1)) >> (self.w - self.k)

        def put(self, key: int, value: int) -> None:
            h = self._hash(key)
            for i, (k, v) in enumerate(self.arr[h]):
                if k == key:
                    self.arr[h][i] = (k, value)
                    return
            self.arr[h].append((key, value))

        def get(self, key: int) -> int:
            h = self._hash(key)
            for i, (k, v) in enumerate(self.arr[h]):
                if k == key:
                    return v
            return -1

        def remove(self, key: int) -> None:
            h = self._hash(key)
            for i, (k, v) in enumerate(self.arr[h]):
                if k == key:
                    self.arr[h].remove((k, v))

    # 705 hashset
    # def add(self, key: int) -> None:
    #     h = self._hash(key)
    #     if key not in self.arr[h]:
    #         self.arr[h].append(key)

    # def remove(self, key: int) -> None:
    #     h = self._hash(key)
    #     if key in self.arr[h]:
    #         self.arr[h].remove(key)

    # def contains(self, key: int) -> bool:
    #     h = self._hash(key)
    #     return key in self.arr[h]


class _283:
    """
    # - Move Zeroes -
    # https://leetcode.com/problems/move-zeroes/
    Given an integer array nums, move all 0's to the end of it while maintaining the
    relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Example 2:
    Input: nums = [0]
    Output: [0]

    Follow up: Could you minimize the total number of operations done?
    """

    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1


class _1004:
    """
    # - Max Consecutive Ones III -
    # https://leetcode.com/problems/max-consecutive-ones-iii/
    """

    ...


class _206:
    """
    # - Reverse Linked List -
    # https://leetcode.com/problems/reverse-linked-list/
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:
    1->2->3->4->5
    1<-2<-3<-4<-5
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Example 2:
    Input: head = [1,2]
    Output: [2,1]

    Example 3:
    Input: head = []
    Output: []
    """

    # NOTE only use node.val and node.next of ListNode

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Iterative method: O(n) time O(1) space"""
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def reverseList_(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive method: O(n) time O(n) space"""
        if not head or not head.next:
            return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail


class _935:
    """
    # - Knight Dialer -
    # https://leetcode.com/problems/knight-dialer/
    """

    ...


class _286:
    """
    # - Walls and Gates -
    # https://leetcode.com/problems/walls-and-gates/
    """

    ...


class _6:
    """
    # - Zigzag Conversion -
    #
    """

    ...


class _1353:
    """
    # - Maximum Number of Events That Can Be Attended -
    # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
    """

    ...


class _348:
    """
    # - Design Tic-Tac-Toe -
    # https://leetcode.com/problems/design-tic-tac-toe/
    """

    ...


class _907:
    """
    # - Sum of Subarray Minimums -
    # https://leetcode.com/problems/sum-of-subarray-minimums/
    """

    ...


class _1283:
    """
    # - Find the Smallest Divisor Given a Threshold -
    # https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
    """

    ...


class _152:
    """
    # - Maximum Product Subarray -
    # https://leetcode.com/problems/maximum-product-subarray/
    Given an integer array nums, find a contiguous non-empty subarray within
    the array that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit
    integer.

    A subarray is a contiguous subsequence of the array.

    Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

    Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    """

    ...


class _43:
    """
    # - Multiply Strings -
    # https://leetcode.com/problems/multiply-strings/
    """

    ...


class _1492:
    """
    # - The kth Factor of n -
    # https://leetcode.com/problems/the-kth-factor-of-n/
    """

    ...


class _341:
    """
    # - Flatten Nested List Iterator -
    # https://leetcode.com/problems/flatten-nested-list-iterator/
    """

    ...


class _1413:
    """
    # - Minimum Value to Get Positive Step by Step Sum -
    # https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
    Given an array of integers nums, you start with an initial positive value startValue.

    In each iteration, you calculate the step by step sum of startValue plus elements in
    nums (from left to right).

    Return the minimum positive value of startValue such that the step by step sum is
    never less than 1.

    Example 1:
    Input: nums = [-3,2,-3,4,2]
    Output: 5
    Explanation: If you choose startValue = 4, in the third iteration your step by step
    sum is less than 1.
    step by step sum
    startValue = 4 | startValue = 5 | nums
    (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
    (1 +2 ) = 3  | (2 +2 ) = 4    |   2
    (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
    (0 +4 ) = 4  | (1 +4 ) = 5    |   4
    (4 +2 ) = 6  | (5 +2 ) = 7    |   2

    Example 2:
    Input: nums = [1,2]
    Output: 1
    Explanation: Minimum start value should be positive.

    Example 3:
    Input: nums = [1,-2,-3]
    Output: 5
    """

    def minStartValue(self, nums: List[int]) -> int:
        """O(n) time O(1) space"""
        ans = prefix = 0
        for x in nums:
            prefix += x
            ans = min(ans, prefix)
        return -ans + 1


class _368:
    """
    # - Largest Divisible Subset -
    # https://leetcode.com/problems/largest-divisible-subset/
    """

    ...


class _300:
    """
    # - Longest Increasing Subsequence -
    # https://leetcode.com/problems/longest-increasing-subsequence/
    Given an integer array nums, return the length of the longest strictly
    increasing subsequence.

    A subsequence is a sequence that can be derived from an array by deleting
    some or no elements without changing the order of the remaining elements.
    For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

    Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore
    the length is 4.

    Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

    Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

    Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

    Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
    complexity?"""

    ...


class _642:
    """
    # - Design Search Autocomplete System -
    # https://leetcode.com/problems/design-search-autocomplete-system/
    """

    ...


class _523:
    """
    # - Continuous Subarray Sum -
    # https://leetcode.com/problems/continuous-subarray-sum/
    """

    ...


class _353:
    """
    # - Design Snake Game -
    # https://leetcode.com/problems/design-snake-game/
    """

    ...


class _2003:
    """
    # - Smallest Missing Genetic Value in Each Subtree -
    # https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/
    """

    ...


class _91:
    """
    # - Decode Ways -
    # https://leetcode.com/problems/decode-ways/
    A message containing letters from A-Z is being encoded to numbers using the
    following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

    Given a non-empty string containing only digits, determine the total number
    of ways to decode it.

    Example 1:
    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).

    Example 2:
    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)."""

    ...


class _72:
    """
    # - Edit Distance -
    # https://leetcode.com/problems/edit-distance/
    Given two strings word1 and word2, return the minimum number of operations
    required to convert word1 to word2.

    You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

    Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

    Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
    """

    ...


class _430:
    """
    # - Flatten a Multilevel Doubly Linked List -
    # https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
    """

    ...


class _143:
    """
    # - Reorder List -
    # https://leetcode.com/problems/reorder-list/
    You are given the head of a singly linked-list. The list can be represented as:

    L0 ??? L1 ??? ??? ??? Ln - 1 ??? Ln
    Reorder the list to be on the following form:

    L0 ??? Ln ??? L1 ??? Ln - 1 ??? L2 ??? Ln - 2 ??? ???
    You may not modify the values in the list's nodes. Only nodes themselves may
    be changed.

    Example 1:
    1 -> 2 -> 3 -> 4
           |
           V
    1 -> 4 -> 2 -> 3

    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

    Example 2:
    1 -> 2 -> 3 -> 4 -> 5
              |
              V
    1 -> 5 -> 2 -> 4 -> 3

    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]
    """

    ...


class _118:
    """
    # - Pascal's Triangle -
    # https://leetcode.com/problems/pascals-triangle/
    """

    ...


class _122:
    """
    # - Best Time to Buy and Sell Stock II -
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    """

    ...


class _242:
    """
    # - Valid Anagram -
    # https://leetcode.com/problems/valid-anagram/
    Given two strings s and t, return true if t is an anagram of s, and
    false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.

    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:
    Input: s = "rat", t = "car"
    Output: false
    """

    ...


class _787:
    """
    # - Cheapest Flights Within K Stops -
    # https://leetcode.com/problems/cheapest-flights-within-k-stops/
    """

    ...


class _609:
    """
    # - Find Duplicate File in System -
    # https://leetcode.com/problems/find-duplicate-file-in-system/
    """

    ...


class _809:
    """
    # - Expressive Words -
    # https://leetcode.com/problems/expressive-words/
    # NOTE poory worded
    Sometimes people repeat letters to represent extra feeling. For example:
        - "hello" -> "heeellooo"
        - "hi" -> "hiiii"

    In these strings like "heeellooo", we have groups of adjacent letters that
    are all the same: "h", "eee", "ll", "ooo".

    You are given a string s and an array of query strings words. A query word
    is stretchy if it can be made to be equal to s by any number of
    applications of the following extension operation: choose a group
    consisting of characters c, and add some number of characters c to the
    group so that the size of the group is three or more.

        - For example, starting with "hello", we could do an extension on the
        group "o" to get "hellooo", but we cannot get "helloo" since the group
        "oo" has a size less than three. Also, we could do another extension
        like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then
        the query word "hello" would be stretchy because of these two extension
        operations: query = "hello" -> "hellooo" -> "helllllooo" = s.

    Return the number of query strings that are stretchy.

    Example 1:
    Input: s = "heeellooo", words = ["hello", "hi", "helo"]
    Output: 1
    Explanation:
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not
    size 3 or more.

    Example 2:
    Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
    Output: 3
    """

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


class _726:
    """
    # - Number of Atoms -
    # https://leetcode.com/problems/number-of-atoms/
    """

    ...


class _472:
    """
    # - Concatenated Words -
    # https://leetcode.com/problems/concatenated-words/
    """

    ...


class _986:
    """
    # - Interval List Intersections -
    # https://leetcode.com/problems/interval-list-intersections/
    """

    ...


class _428:
    """
    # - Serialize and Deserialize N-ary Tree -
    # https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
    """

    ...


class _127:
    """
    # - Word Ladder -
    # https://leetcode.com/problems/word-ladder/
    """

    ...


class _128:
    """
    # - Longest Consecutive Sequence -
    # https://leetcode.com/problems/longest-consecutive-sequence/
    Given an unsorted array of integers nums, return the length of the longest
    consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

    Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    """

    ...


class _658:
    """
    # - Find K Closest Elements -
    # https://leetcode.com/problems/find-k-closest-elements/
    Given a sorted integer array arr, two integers k and x, return the k
    closest integers to x in the array. The result should also be sorted
    in ascending order.

    An integer a is closer to x than an integer b if:
        |a - x| < |b - x|, or
        |a - x| == |b - x| and a < b

    Example 1:
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

    Example 2:
    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]

    NOTE arr is sorted in ascending order.
    """

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]


class _1047:
    """
    # - Remove All Adjacent Duplicates In String -
    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
    You are given a string s consisting of lowercase English letters. A duplicate
    removal consists of choosing two adjacent and equal letters and removing them.

    We repeatedly make duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. It
    can be proven that the answer is unique.

    Example 1:
    Input: s = "abbaca"
    Output: "ca"
    Explanation: For example, in "abbaca" we could remove "bb" since the letters
    are adjacent and equal, and this is the only possible move.  The result of
    this move is that the string is "aaca", of which only "aa" is possible, so
    the final string is "ca".

    Example 2:
    Input: s = "azxxzy"
    Output: "ay"
    """

    def removeDuplicates(self, s: str) -> str:
        output = []
        for char in s:
            if output and char == output[-1]:
                output.pop()
            else:
                output.append(char)
        return "".join(output)


class _173:
    """
    # - Binary Search Tree Iterator -
    # https://leetcode.com/problems/binary-search-tree-iterator/
    """

    ...


class _1381:
    """
    # - Design a Stack With Increment Operation -
    # https://leetcode.com/problems/design-a-stack-with-increment-operation/
    """

    ...


class _356:
    """
    # - Line Reflection -
    # https://leetcode.com/problems/line-reflection/
    Given n points on a 2D plane, find if there is such a line parallel to
    the y-axis that reflects the given points symmetrically.

    In other words, answer whether or not if there exists a line that after
    reflecting all points over the given line, the original points' set is
    the same as the reflected ones.

    Note that there can be repeated points.

    Example 1:
    Input: points = [[1,1],[-1,1]]
    Output: true
    Explanation: We can choose the line x = 0.

    Example 2:
    Input: points = [[1,1],[-1,-1]]
    Output: false
    Explanation: We can't choose a line.
    """

    def isReflected(self, points: List[List[int]]) -> bool:
        points_set = set(tuple(p) for p in points)
        xs = [x for x, _ in points_set]
        x0 = (min(xs) + max(xs)) / 2
        return all(((2 * x0 - x, y) in points_set) for x, y in points_set)


class _1015:
    """
    # - Smallest Integer Divisible by K -
    # https://leetcode.com/problems/smallest-integer-divisible-by-k/
    Given a positive integer k, you need to find the length of the smallest
    positive integer n such that n is divisible by k, and n only contains
    the digit 1.

    Return the length of n. If there is no such n, return -1.

    Note: n may not fit in a 64-bit signed integer.

    Example 1:
    Input: k = 1
    Output: 1
    Explanation: The smallest answer is n = 1, which has length 1.

    Example 2:
    Input: k = 2
    Output: -1
    Explanation: There is no such positive integer n divisible by 2.

    Example 3:
    Input: k = 3
    Output: 3
    Explanation: The smallest answer is n = 111, which has length 3.
    """

    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 not in {1, 3, 7, 9}:
            return -1
        mod, mod_set = 0, set()
        for length in range(1, k + 1):
            mod = (10 * mod + 1) % k
            if mod == 0:
                return length
            if mod in mod_set:
                return -1  # Pigeonhole principle there will be loop
            mod_set.add(mod)
        return -1


class _155:
    """
    # - Min Stack -
    # https://leetcode.com/problems/min-stack/
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

    You must implement a solution with O(1) time complexity for each function.
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        temp_minimum = self.stack[-1][1]
        self.stack.append((val, min(temp_minimum, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class _202:
    """
    # - Happy Number -
    # https://leetcode.com/problems/happy-number/
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:
    * Starting with any positive integer, replace the number by the sum of the
    squares of its digits.
    * Repeat the process until the number equals 1 (where it will stay), or it
    loops endlessly in a cycle which does not include 1.
    * Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

    Example 1:
    Input: n = 19
    Output: true
    Explanation:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

    Example 2:
    Input: n = 2
    Output: false
    """

    def fn(self, n: int) -> int:
        """O(logn) time O(1) space"""
        # NOTE Finding the next value for a given number has a cost of O(logn)
        # because we are processing each digit in the number, and the number of
        # digits in a number is given by logn.
        ans = 0
        while n > 0:
            n, digit = divmod(n, 10)
            ans += digit**2
        return ans

    def isHappy(self, n: int) -> bool:
        """Floyd's cycle detection method: O(logn) space O(1) space"""
        slow = n
        fast = self.fn(n)
        while fast != 1 and slow != fast:
            slow = self.fn(slow)
            fast = self.fn(self.fn(fast))
        return fast == 1

    def isHappy_(self, n: int) -> bool:
        """Hashset method: O(logn) time O(logn) space"""
        seen = set()
        while n != 1 and n not in seen:
            # NOTE we dont have to deal with the case where the number always increases
            # because we know it always decreases or loops
            # thus notice the number of digits in n will shrink by 1 each iteration
            # meaning n decreases by logn.
            seen.add(n)
            n = self.fn(n)
        return n == 1


class _862:
    """
    # - Shortest Subarray with Sum at Least K -
    # https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
    """

    ...


class _503:
    """
    # - Next Greater Element II -
    # https://leetcode.com/problems/next-greater-element-ii
    """

    ...


class _218:
    """
    # - The Skyline Problem -
    # https://leetcode.com/problems/the-skyline-problem/
    """

    ...


class _678:
    """
    # - Valid Parenthesis String -
    # https://leetcode.com/problems/valid-parenthesis-string/
    """

    ...


class _349:
    """
    # - Intersection of Two Arrays -
    # https://leetcode.com/problems/intersection-of-two-arrays/
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

    Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

    Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """O(max(m,n)) avg case O(m*n) worst case time O(m+n) space"""
        # NOTE The worse case is if the set decays into linear searching buckets
        #      https://wiki.python.org/moin/TimeComplexity#set
        return list(set(nums1) & set(nums2))


class _2008:
    """
    # - Maximum Earnings From Taxi -
    # https://leetcode.com/problems/maximum-earnings-from-taxi/
    """

    ...


class _493:
    """
    # - Reverse Pairs -
    # https://leetcode.com/problems/reverse-pairs/
    """

    ...


class _1344:
    """
    # - Angle Between Hands of a Clock -
    # https://leetcode.com/problems/angle-between-hands-of-a-clock/
    """

    ...


class _8:
    """
    # - String to Integer (atoi) -
    # https://leetcode.com/problems/string-to-integer-atoi/
    """

    ...


class _427:
    """
    # - Construct Quad Tree -
    # https://leetcode.com/problems/construct-quad-tree/
    """

    ...


class _489:
    """
    # - Robot Room Cleaner -
    # https://leetcode.com/problems/robot-room-cleaner/
    """

    ...


class _843:
    """
    # - Guess the Word -
    # https://leetcode.com/problems/guess-the-word/
    """

    ...


class _1166:
    """
    # - Design File System -
    # https://leetcode.com/problems/design-file-system/
    """

    ...


class _724:
    """
    # - Find Pivot Index -
    # https://leetcode.com/problems/find-pivot-index/
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left
    of the index is equal to the sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there
    are no elements to the left. This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

    Example 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11

    Example 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.

    Example 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0
    """

    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, sum_nums = 0, sum(nums)
        for i, num in enumerate(nums):
            if left_sum == sum_nums - left_sum - num:
                return i
            left_sum += num
        return -1


class _772:
    """
    # - Basic Calculator III -
    # https://leetcode.com/problems/basic-calculator-iii/
    """

    ...


class _1539:
    """
    # - Kth Missing Positive Number -
    # https://leetcode.com/problems/kth-missing-positive-number/
    Given an array arr of positive integers sorted in a strictly increasing
    order, and an integer k.

    Find the kth positive integer that is missing from this array.

    Example 1:
    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
    5th missing positive integer is 9.

    Example 2:
    Input: arr = [1,2,3,4], k = 2
    Output: 6
    Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing
    positive integer is 6.
    """

    # TODO revisit all the binary search problems
    #      my grasp of this one is finicky

    def findKthPositive(self, arr: List[int], k: int) -> int:
        """O(logn) time O(1) space"""
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1
        return left + k


class _98:
    r"""
    # - Validate Binary Search Tree -
    # https://leetcode.com/problems/validate-binary-search-tree/
    Given the root of a binary tree, determine if it is a valid binary search
    tree (BST).

    A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than the
        node's key.
        - The right subtree of a node contains only nodes with keys greater than the
        node's key.
        - Both the left and right subtrees must also be binary search trees.


    Example 1:
        2
       / \
      1   3
    Input: root = [2,1,3]
    Output: true

    Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
    """
    ...


class _75:
    """
    # - Sort Colors -
    # https://leetcode.com/problems/sort-colors/
    """

    ...


class _791:
    """
    # - Custom Sort String -
    # https://leetcode.com/problems/custom-sort-string/
    """

    ...


class _167:
    """
    # - Two Sum II - Input Array Is Sorted -
    #
    """

    ...


class _67:
    """
    # - Add Binary -
    # https://leetcode.com/problems/add-binary/
    """

    ...


class _1405:
    """
    # - Longest Happy String -
    # https://leetcode.com/problems/longest-happy-string/
    """

    ...


class _419:
    """
    # - Battleships in a Board -
    # https://leetcode.com/problems/battleships-in-a-board/
    """

    ...


class _85:
    """
    # - Maximal Rectangle -
    # https://leetcode.com/problems/maximal-rectangle/
    """

    ...


class _249:
    """
    # - Group Shifted Strings -
    # https://leetcode.com/problems/group-shifted-strings/
    """

    ...


class _616:
    """
    # - Add Bold Tag in String -
    # https://leetcode.com/problems/add-bold-tag-in-string/
    """

    ...


class _416:
    """
    # - Partition Equal Subset Sum -
    # https://leetcode.com/problems/partition-equal-subset-sum/
    """

    ...


class _96:
    """
    # - Unique Binary Search Trees -
    # https://leetcode.com/problems/unique-binary-search-trees/
    """

    ...


class _336:
    """
    # - Palindrome Pairs -
    # https://leetcode.com/problems/palindrome-pairs/
    """

    ...


class _179:
    """
    # - Largest Number -
    # https://leetcode.com/problems/largest-number/
    """

    ...


class _1029:
    """
    # - Two City Scheduling -
    # https://leetcode.com/problems/two-city-scheduling/
    """

    ...


class _1481:
    """
    # - Least Number of Unique Integers after K Removals -
    # https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
    """

    ...


class _2104:
    """
    # - Sum of Subarray Ranges -
    # https://leetcode.com/problems/sum-of-subarray-ranges/
    You are given an integer array nums. The range of a subarray of nums is
    the difference between the largest and smallest element in the subarray.

    Return the sum of all subarray ranges of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:
    Input: nums = [1,2,3]
    Output: 4
    Explanation: The 6 subarrays of nums are the following:
    [1], range = largest - smallest = 1 - 1 = 0
    [2], range = 2 - 2 = 0
    [3], range = 3 - 3 = 0
    [1,2], range = 2 - 1 = 1
    [2,3], range = 3 - 2 = 1
    [1,2,3], range = 3 - 1 = 2
    So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

    Example 2:
    Input: nums = [1,3,3]
    Output: 4
    Explanation: The 6 subarrays of nums are the following:
    [1], range = largest - smallest = 1 - 1 = 0
    [3], range = 3 - 3 = 0
    [3], range = 3 - 3 = 0
    [1,3], range = 3 - 1 = 2
    [3,3], range = 3 - 3 = 0
    [1,3,3], range = 3 - 1 = 2
    So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

    Example 3:
    Input: nums = [4,-2,-3,4,1]
    Output: 59
    Explanation: The sum of all subarray ranges of nums is 59.
    """

    ...


class _166:
    """
    # - Fraction to Recurring Decimal -
    # https://leetcode.com/problems/fraction-to-recurring-decimal/
    """

    ...


class _432:
    """
    # - All O`one Data Structure -
    #
    """

    ...


class _149:
    """
    # - Max Points on a Line -
    # https://leetcode.com/problems/max-points-on-a-line/
    """

    ...


class _346:
    """
    # - Moving Average from Data Stream -
    # https://leetcode.com/problems/moving-average-from-data-stream/
    Given a stream of integers and a window size, calculate the moving average of
    all integers in the sliding window.

    Implement the MovingAverage class:
    * MovingAverage(int size) Initializes the object with the size of the window size.
    * double next(int val) Returns the moving average of the last size values of the
    stream.

    Example 1:
    Input
    ["MovingAverage", "next", "next", "next", "next"]
    [[3], [1], [10], [3], [5]]
    Output
    [null, 1.0, 5.5, 4.66667, 6.0]

    Explanation
    MovingAverage movingAverage = new MovingAverage(3);
    movingAverage.next(1); // return 1.0 = 1 / 1
    movingAverage.next(10); // return 5.5 = (1 + 10) / 2
    movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
    movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
    """

    class MovingAverage:
        """Queue method: O(1) time O(n) space"""

        def __init__(self, size: int):
            self.nums = deque()
            self.size = size
            self.window_sum = 0

        def next(self, val: int) -> float:
            self.nums.append(val)
            self.window_sum += val
            if len(self.nums) > self.size:
                self.window_sum -= self.nums.popleft()
            return self.window_sum / len(self.nums)

    class MovingAverage_:
        """Circular queue (array) method: O(1) time O(n) space"""

        # NOTE tail = (head + 1) mod size
        #      in a circular queue:
        #   -> [ ] [H] | [T] [ ] <-
        #   |                     |
        #   -----------------------

        def __init__(self, size: int):
            self.size = size
            self.arr = [0] * self.size
            self.head = self.window_sum = 0
            self.count = 0

        def next(self, val: int) -> float:
            self.count += 1
            tail = (self.head + 1) % self.size
            self.window_sum = self.window_sum - self.arr[tail] + val
            self.head = (self.head + 1) % self.size  # head eats tail
            self.arr[self.head] = val
            return self.window_sum / min(self.size, self.count)


class _1275:
    """
    # - Find Winner on a Tic Tac Toe Game -
    # https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
    Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules
    of Tic-Tac-Toe are:
    * Players take turns placing characters into empty squares ' '.
    * The first player A always places 'X' characters, while the second
    player B always places 'O' characters.
    * 'X' and 'O' characters are always placed into empty squares, never on
    filled ones.
    * The game ends when there are three of the same (non-empty) character
    filling any row, column, or diagonal.
    * The game also ends if all squares are non-empty.
    * No more moves can be played if the game is over.

    Given a 2D integer array moves where moves[i] = [rowi, coli] indicates
    that the ith move will be played on grid[rowi][coli]. return the winner
    of the game if it exists (A or B). In case the game ends in a draw
    return "Draw". If there are still movements to play return "Pending".

    You can assume that moves is valid (i.e., it follows the rules of
    Tic-Tac-Toe), the grid is initially empty, and A will play first.

    Example 1:
    x
     x
    oox
    Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    Output: "A"
    Explanation: A wins, they always play first.

    Example 2:
    xxo
    xo
    o
    Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    Output: "B"
    Explanation: B wins.

    Example 3:
    xxo
    oox
    xox
    Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    Output: "Draw"
    Explanation: The game ends in a draw since there are no moves to make.
    """

    def tictactoe(self, moves: List[List[int]]) -> str:
        """O(m) time O(n) space, where m is len moves, n is size board"""
        rows, cols, diag, anti = [0] * 3, [0] * 3, 0, 0
        for turn, (x, y) in enumerate(moves):
            player = (turn % 2) * 2 - 1
            rows[x] += player
            cols[y] += player
            if x == y:
                diag += player
            if x + y == 2:
                anti += player
            if any(abs(win) == 3 for win in [rows[x], cols[y], diag, anti]):
                return "B" if player == 1 else "A"
        return "Draw" if len(moves) == 9 else "Pending"


class _480:
    """
    # - Sliding Window Median -
    # https://leetcode.com/problems/sliding-window-median/
    """

    ...


class _26:
    """
    # - Remove Duplicates from Sorted Array -
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    """

    ...


class _241:
    """
    # - Different Ways to Add Parentheses -
    # https://leetcode.com/problems/different-ways-to-add-parentheses/
    """

    ...


class _301:
    """
    # - Remove Invalid Parentheses -
    # https://leetcode.com/problems/remove-invalid-parentheses/
    """

    ...


class _73:
    """
    # - Set Matrix Zeroes -
    # https://leetcode.com/problems/set-matrix-zeroes/
    Given an m x n integer matrix matrix, if an element is 0, set its entire row
    and column to 0's.

    You must do it in place.

    Example 1:
    1 1 1    1 0 1
    1 0 1 -> 0 0 0
    1 1 1    1 0 1
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Example 2:
    0 1 2 0    0 0 0 0
    3 4 5 2 -> 0 4 5 0
    1 3 1 5    0 3 1 0
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    """

    ...


class _1647:
    """
    # - Minimum Deletions to Make Character Frequencies Unique -
    # https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
    """

    ...


class _1366:
    """
    # - Rank Teams by Votes -
    # https://leetcode.com/problems/rank-teams-by-votes/
    """

    ...


class _279:
    """
    # - Perfect Squares -
    # https://leetcode.com/problems/perfect-squares/
    """

    ...


class _403:
    """
    # - Frog Jump -
    # https://leetcode.com/problems/frog-jump/
    """

    ...


class _621:
    """
    # - Task Scheduler -
    # https://leetcode.com/problems/task-scheduler/
    """

    ...


class _741:
    """
    # - Cherry Pickup -
    # https://leetcode.com/problems/cherry-pickup/
    """

    ...


class _19:
    """
    # - Remove Nth Node From End of List -
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    """

    ...


class _99:
    """
    # - Recover Binary Search Tree -
    # https://leetcode.com/problems/recover-binary-search-tree/
    """

    ...


class _526:
    """
    # - Beautiful Arrangement -
    # https://leetcode.com/problems/beautiful-arrangement/
    """

    ...


class _647:
    """
    # - Palindromic Substrings -
    # https://leetcode.com/problems/palindromic-substrings/
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.

    Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

    Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    """

    ...


class _93:
    """
    # - Restore IP Addresses -
    # https://leetcode.com/problems/restore-ip-addresses/
    """

    ...


class _496:
    """
    # - Next Greater Element I -
    # https://leetcode.com/problems/next-greater-element-i/
    """

    ...


class _953:
    """
    # - Verifying an Alien Dictionary -
    # https://leetcode.com/problems/verifying-an-alien-dictionary/
    """

    ...


#########################################################################################
# - Sub 300 (most of them at least) -


class _977:
    """
    # - Squares of a Sorted Array -
    # https://leetcode.com/problems/squares-of-a-sorted-array/
    Given an integer array nums sorted in non-decreasing order, return an array
    of the squares of each number sorted in non-decreasing order.

    Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

    Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

    NOTE nums is sorted in non-decreasing order.
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """O(n) time O(n) space"""
        n = len(nums)
        ans = [0] * n
        left, right = 0, n - 1
        for i in reversed(range(n)):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            ans[i] = square**2
        return ans


class _1304:
    """
    # - Find N Unique Integers Sum up to Zero -
    # https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
    Given an integer n, return any array containing n unique integers such that they add up to 0.

    Example 1:
    Input: n = 5
    Output: [-7,-1,1,3,4]
    Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

    Example 2:
    Input: n = 3
    Output: [-1,0,1]
    Example 3:

    Input: n = 1
    Output: [0]
    """

    def sumZero(self, n: int) -> List[int]:
        return [x for x in range(1 - n, n, 2)]


class _1332:
    """
    # - Remove Palindromic Subsequences -
    # https://leetcode.com/problems/remove-palindromic-subsequences/
    You are given a string s consisting only of letters 'a' and 'b'. In a
    single step you can remove one palindromic subsequence from s.

    Return the minimum number of steps to make the given string empty.

    A string is a subsequence of a given string if it is generated by
    deleting some characters of a given string without changing its order.
    Note that a subsequence does not necessarily need to be contiguous.

    A string is called palindrome if is one that reads the same backward
    as well as forward.

    Example 1:
    Input: s = "ababa"
    Output: 1
    Explanation: s is already a palindrome, so its entirety can be
    removed in a single step.

    Example 2:
    Input: s = "abb"
    Output: 2
    Explanation: "abb" -> "bb" -> "".
    Remove palindromic subsequence "a" then "bb".

    Example 3:
    Input: s = "baabb"
    Output: 2
    Explanation: "baabb" -> "b" -> "".
    Remove palindromic subsequence "baab" then "b".
    """

    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome():
            """O(n) time O(1) space"""
            lo, hi = 0, len(s) - 1
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        return 2 - int(is_palindrome()) - (s == "")

    def _is_palindrome(self, s):
        """O(n) time O(n) space"""
        return 2 - (s == s[::-1]) - (s == "")


class _867:
    """
    # - Transpose Matrix -
    # https://leetcode.com/problems/transpose-matrix/
    Given a 2D integer array matrix, return the transpose of matrix.

    The transpose of a matrix is the matrix flipped over its main diagonal,
    switching the matrix's row and column indices.

    Example 1:

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]
    Example 2:

    Input: matrix = [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(x) for x in list(zip(*matrix))]

    def _transpose(self, matrix):
        ans = [[None] * len(matrix) for _ in range(len(matrix[0]))]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans


class _1260:
    """
    # - Shift 2D Grid -
    # https://leetcode.com/problems/shift-2d-grid/
    Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

    In one shift operation:

    Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0].
    Element at grid[m - 1][n - 1] moves to grid[0][0].
    Return the 2D grid after applying shift operation k times.

    Example 1:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]

    Example 2:
    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

    Example 3:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]
    """

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                new_col = (c + k) % n
                wrap_around_count = (c + k) // n
                new_row = (r + wrap_around_count) % m
                new_grid[new_row][new_col] = grid[r][c]
        return new_grid


class _1822:
    """
    There is a function signFunc(x) that returns:
        1 if x is positive.
        -1 if x is negative.
        0 if x is equal to 0.
    You are given an integer array nums. Let product be the product of all
    values in the array nums. Return signFunc(product).

    Example 1:
    Input: nums = [-1,-2,-3,-4,3,2,1]
    Output: 1
    Explanation: The product of all values in the array is 144, and
    signFunc(144) = 1

    Example 2:
    Input: nums = [1,5,0,2,-3]
    Output: 0
    Explanation: The product of all values in the array is 0, and
    signFunc(0) = 0

    Example 3:
    Input: nums = [-1,1,-1,1,-1]
    Output: -1
    Explanation: The product of all values in the array is -1, and
    signFunc(-1) = -1
    """

    def arraySign(self, nums: List[int]) -> int:
        """O(n) time, O(1) space"""
        ans = reduce(lambda x, y: x * y, nums)
        return 0 if not ans else 1 if ans > 0 else -1

    def _arraySign(self, nums: List[int]) -> int:
        """Same as above with early out"""
        ans = 1
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                ans *= -1
        return ans


class _383:
    """
    # - 383. Ransom Note -
    # https://leetcode.com/problems/ransom-note/
    Given two strings ransomNote and magazine, return true if ransomNote can be
    constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

    Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

    Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """O(n) time, O(k)/O(1) space, k is a constant 26"""
        if len(ransomNote) > len(magazine):
            return False
        letters = Counter(magazine)
        for c in ransomNote:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        return True

        # NOTE there is a time complexity solutions but...


class _243:
    """
    # - 243. Shortest Word Distance -
    # https://leetcode.com/problems/shortest-word-distance/
    Given an array of strings wordsDict and two different strings that already
    exist in the array word1 and word2, return the shortest distance between
    these two words in the list.

    Example 1:
    Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
    word1 = "coding", word2 = "practice"
    Output: 3

    Example 2:
    Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"],
    word1 = "makes", word2 = "coding"
    Output: 1
    """

    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """O(n) time O(1) space"""
        ans = i1 = i2 = inf
        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            ans = min(ans, abs(i1 - i2))
        return ans  # type: ignore


class _204:
    """
    # - 205. Isomorphic Strings -
    # https://leetcode.com/problems/isomorphic-strings/
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced
    to get t.

    All occurrences of a character must be replaced with another character
    while preserving the order of characters. No two characters may map to
    the same character, but a character may map to itself.

    Example 1:
    Input: s = "egg", t = "add"
    Output: true

    Example 2:
    Input: s = "foo", t = "bar"
    Output: false

    Example 3:
    Input: s = "paper", t = "title"
    Output: true
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        """O(n) time O(1) space"""
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

    def _isIsomorphic(self, s: str, t: str) -> bool:
        """O(n) time O(n) space"""

        def fn(s: str) -> List[str]:
            index_mp = {}
            ans = []
            for i, c in enumerate(s):
                if c not in index_mp:
                    index_mp[c] = i
                ans.append(str(index_mp[c]))
            return ans

        return fn(s) == fn(t)


class _1360:
    """
    # - 1360. Number of Days Between Two Dates -
    # https://leetcode.com/problems/number-of-days-between-two-dates/
    Write a program to count the number of days between two dates.

    The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

    Example 1:
    Input: date1 = "2019-06-29", date2 = "2019-06-30"
    Output: 1

    Example 2:
    Input: date1 = "2020-01-15", date2 = "2019-12-31"
    Output: 15
    """

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        ans = abs((d2 - d1).days)
        return ans


class _231:
    """
    # - 231. Power of Two -
    # https://leetcode.com/problems/power-of-two/
    Given an integer n, return true if it is a power of two. Otherwise, return false.

    An integer n is a power of two, if there exists an integer x such that n == 2x.

    Example 1:
    Input: n = 1
    Output: true
    Explanation: 20 = 1

    Example 2:
    Input: n = 16
    Output: true
    Explanation: 24 = 16

    Example 3:
    Input: n = 3
    Output: false
    """

    def isPowerOfTwo(self, n: int) -> bool:
        """O(1) time O(1) space"""
        if n == 0:
            return False
            # remember in two's complement -x is ~x + 1
            # now remember binary is powers of twos
        return n & (-n) == n

    def _isPowerOfTwo(self, n: int) -> bool:
        """O(1) time O(1) space"""
        return n > 0 and bin(n).count("1") == 1


class _869:
    """
    # - 869. Reordered Power of 2 -
    # https://leetcode.com/problems/reordered-power-of-2/
    You are given an integer n. We reorder the digits in any order (including the
    original order) such that the leading digit is not zero.

    Return true if and only if we can do this so that the resulting number is a
    power of two.

    Example 1:
    Input: n = 1
    Output: true

    Example 2:
    Input: n = 10
    Output: false
    """

    def reorderedPowerOf2(self, n: int) -> bool:
        """O((logn)! * logn) time O(logn) space, simple solution"""
        return any(
            x[0] != "0" and bin(int("".join(x))).count("1") == 1
            for x in permutations(str(n))
        )

    def _reorderedPowerOf2(self, n: int) -> bool:
        """O(log^2n) time O(logn) space, cheeky solution"""
        count = Counter(str(n))
        return any(count == Counter(str(1 << x)) for x in range(31))


class _905:
    """
    # - 905. Sort Array By Parity -
    # https://leetcode.com/problems/sort-array-by-parity/
    Given an integer array nums, move all the even integers at the beginning
    of the array followed by all the odd integers.

    Return any array that satisfies this condition.

    Example 1:
    Input: nums = [3,1,2,4]
    Output: [2,4,3,1]
    Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would
    also be accepted.

    Example 2:
    Input: nums = [0]
    Output: [0]
    """

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """O(n) time O(n) space, one pass"""
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0:
                i += 1
            else:
                j -= 1
        return A

    def _sortArrayByParity(self, A: List[int]) -> List[int]:
        """O(n) time O(n) space, two pass"""
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]

    def __sortArrayByParity(self, A: List[int]) -> List[int]:
        """O(nlogn) time O(n) space"""
        A.sort(key=lambda x: x % 2)
        return A
