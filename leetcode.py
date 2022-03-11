from __future__ import annotations

import re
from bisect import bisect_left
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
from heapq import heapify, heappop, heappush, nlargest
from itertools import chain, product
from math import comb, inf
from typing import Callable, Deque, Dict, Final, List, Optional, Set, Tuple, Union


class Array:
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
        raise Exception

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

    def containsDuplicate(self, nums: List[int]) -> bool:
        """O(n) time, O(n) space"""
        return len(nums) != len(set(nums))

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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """O(n) time, O(1) space (excluding output array)"""
        ans = [1] * len(nums)
        prefix = suffix = 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]
            ans[~i] *= suffix
            suffix *= nums[~i]
        return ans

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

    def maxProduct(self, nums: List[int]) -> int:
        """O(n) time, O(1) space"""
        if len(nums) == 0:
            return 0
        ans = mn = mx = nums[0]
        for num in nums[1:]:
            mn, mx = min(num, mn * num, mx * num), max(num, mn * num, mx * num)
            ans = max(mx, ans)
        return ans

    """
    # - Find Minimum in Rotated Sorted Array -
    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    Suppose an array of length n sorted in ascending order is rotated between 1
    and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time
    results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum
    element of this array.

    You must write an algorithm that runs in O(log n) time.

    Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.

    Example 2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4
    times.

    Example 3:
    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] and it was rotated 4
    times.
    """

    def findMin(self, nums: List[int]) -> int:
        """O(log(n)) time, O(1) space"""
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]

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

    def search(self, nums: List[int], target: int) -> int:
        """O(log(n)) time, O(1) space"""
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """no sort version O(n^2) time, O(n)"""
        res, dups = set(), set()
        seen: Dict[int, int] = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i + 1 :]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(list(sorted((val1, val2, complement))))
                    seen[val2] = i
        return list(res)

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

    def _threeSum(self, nums: List[int]) -> List[List[int]]:
        """sort version O(n^2) time, O(n)"""
        res: List[List[int]] = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

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

    def maxArea(self, height: List[int]) -> int:
        """O(n) time, O(1) space"""
        m, i, j = 0, 0, len(height) - 1
        while i < j:
            m = max(m, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m


class Binary:
    """
    # - Sum of Two Integers -
    # https://leetcode.com/problems/sum-of-two-integers/
    Given two integers a and b, return the sum of the two integers without
    using the operators + and -.

    Example 1:
    Input: a = 1, b = 2
    Output: 3

    Example 2:
    Input: a = 2, b = 3
    Output: 5
    """

    # ;^)
    # import operator; return operator.add(a, b)
    # return a.__add__(b)
    # return sum([a, b])

    def getSum(self, a: int, b: int) -> int:
        """O(1) time, O(1) space"""
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1
        if a * b >= 0:
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        return x * sign

    """
    # - Number of 1 Bits -
    # https://leetcode.com/problems/number-of-1-bits/
    Write a function that takes an unsigned integer and returns the number of '1'
    bits it has (also known as the Hamming weight).

    Note:

    Note that in some languages, such as Java, there is no unsigned integer type.
    In this case, the input will be given as a signed integer type. It should not
    affect your implementation, as the integer's internal binary representation is
    the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement
    notation. Therefore, in Example 3, the input represents the signed integer. -3.

    Example 1:
    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a
    total of
    three '1' bits.

    Example 2:
    Input: n = 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a
    total of
    one '1' bit.

    Example 3:
    Input: n = 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a
    total of
    thirty one '1' bits.
    """

    def hammingWeight(self, n: int) -> int:
        """O(1)* time, O(1) space *for fixed 32 bit input"""
        return bin(n).count("1")

    def _hammingWeight(self, n: int) -> int:
        """O(1)* time, O(1) space *for fixed 32 bit input)"""
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

    """# - Counting Bits -
    # https://leetcode.com/problems/counting-bits/
    Given an integer n, return an array ans of length n + 1 such that for each i
    (0 <= i <= n), ans[i] is the number of 1's in the binary
    representation of i.

    Example 1:

    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    Example 2:

    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

    Constraints:

    0 <= n <= 105

    Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n).
    Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like
    __builtin_popcount in C++)?"""

    def countBits(self, n: int) -> List[int]:
        """O(n) time, O(1)* space *exclude outout"""
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans

    """# - Missing Number -
    # https://leetcode.com/problems/missing-number/
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.

    Example 1:

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the
    range [0,3]. 2 is the missing number in the range since it does not
    appear in nums.

    Example 2:

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the
    range [0,2]. 2 is the missing number in the range since it does not
    appear in nums.

    Example 3:

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the
    range [0,9]. 8 is the missing number in the range since it does not
    appear in nums.

    Constraints:

    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.

    Follow up: Could you implement a solution using only O(1) extra space
    complexity and O(n) runtime complexity?"""

    def missingNumber(self, nums):
        """XOR solution O(n) time, O(1) space"""
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    def _missingNumber(self, nums: List[int]) -> int:
        """gauss formula O(n) time, O(1) space"""
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    """# - Reverse Bits -
    # https://leetcode.com/problems/reverse-bits/
    Reverse bits of a given 32 bits unsigned integer.

    Note that in some languages, such as Java, there is no unsigned integer
    type. In this case, both input and output will be given as a signed
    integer type. They should not affect your implementation, as the
    integer's internal binary representation is the same, whether it is
    signed or unsigned.

    In Java, the compiler represents the signed integers using 2's complement
    notation. Therefore, in Example 2 above, the input represents the signed
    integer -3 and the output represents the signed integer -1073741825.

    Example 1:

    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    Explanation: The input binary string 00000010100101000001111010011100
    represents the unsigned integer 43261596, so return 964176192 which its
    binary representation is 00111001011110000010100101000000.

    Example 2:

    Input: n = 11111111111111111111111111111101
    Output:   3221225471 (10111111111111111111111111111111)
    Explanation: The input binary string 11111111111111111111111111111101
    represents the unsigned integer 4294967293, so return 3221225471 which
    its binary representation is 10111111111111111111111111111111.

    Constraints:

    The input must be a binary string of length 32

    Follow up: If this function is called many times, how would you optimize
    it?"""

    def reverseBits(self, n: int) -> int:
        """;^) python solution O(1) time, O(1) space"""
        return int(bin(n)[2:].zfill(32)[::-1], 2)

    def reverseBits_(self, n):
        """32 loops solution O(1) time, O(1) space"""
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

    def reverseBits__(self, n: int) -> int:
        """no loop solution O(1) time, O(1) space"""
        n = (n >> 16) | (n << 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        return n

    def reverseBits___(self, n: int) -> int:
        """no loop solution O(1) time, O(1) space"""
        n = (n >> 16) | (n << 16)
        n = ((n & 0b11111111000000001111111100000000) >> 8) | (
            (n & 0b00000000111111110000000011111111) << 8
        )
        n = ((n & 0b11110000111100001111000011110000) >> 4) | (
            (n & 0b00001111000011110000111100001111) << 4
        )
        n = ((n & 0b11001100110011001100110011001100) >> 2) | (
            (n & 0b00110011001100110011001100110011) << 2
        )
        n = ((n & 0b10101010101010101010101010101010) >> 1) | (
            (n & 0b01010101010101010101010101010101) << 1
        )
        return n

    # Dynamic Programming

    """# - Climbing Stairs -
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

    def climbStairs(self, n: int) -> int:
        """O(n) time, O(n) space"""

        @lru_cache(maxsize=None)
        def fn(k: int) -> int:
            if k <= 1:
                return 1
            return fn(k - 1) + fn(k - 2)

        return fn(n)

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

    def coinChange(self, coins: List[int], amount: int) -> int:
        """O(S * n) time, O(S) space
        where S is amount n is denomination count"""

        @lru_cache(maxsize=None)
        def fn(x: int) -> Union[float, int]:
            if x == 0:
                return 0
            if x < 0:
                return inf
            return min(1 + fn(x - coin) for coin in coins)

        fn_amount = fn(amount)
        return fn_amount if isinstance(fn_amount, int) else -1

    """# - Longest Increasing Subsequence -
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

    def lengthOfLIS(self, nums: List[int]) -> int:
        arr: List[int] = []
        for num in nums:
            i = bisect_left(arr, num)
            if i == len(arr):
                arr.append(num)
            else:
                arr[i] = num
        return len(arr)

    """# - Longest Common Subsequence -
    # https://leetcode.com/problems/longest-common-subsequence/
    Given two strings text1 and text2, return the length of their longest
    common subsequence. If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original
    string with some characters (can be none) deleted without changing the
    relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde". A common subsequence of
    two strings is a subsequence that is common to both strings.

    Example 1:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

    Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

    Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.

    Constraints:
    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters."""

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """nuts O(idk)"""
        # stores the smallest index of end of subseq of len i+1
        arr: List[int] = []
        d = defaultdict(list)
        for i, char in enumerate(text2):
            d[char].append(i)
        for char in text1:
            if char in d:
                for i in reversed(d[char]):
                    ins = bisect_left(arr, i)
                    if ins == len(arr):
                        arr.append(i)
                    else:
                        arr[ins] = i
        return len(arr)

    def longestCommonSubsequence_(self, text1: str, text2: str) -> int:
        """memoization recursion solution O(m*n) time, O(m*n) space
        where m, n len of strs"""

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

        return memo_solve(0, 0)

    def longestCommonSubsequence__(self, text1: str, text2: str) -> int:
        """iteration solution O(m*n) time, O(m*n) space
        where m, n len of strs"""
        grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for c in reversed(range(len(text2))):
            for r in reversed(range(len(text1))):
                if text2[c] == text1[r]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                else:
                    grid[r][c] = max(grid[r + 1][c], grid[r][c + 1])
        return grid[0][0]

    """# - Word Break Problem -
    # https://leetcode.com/problems/word-break/
    Given a string s and a dictionary of strings wordDict, return true if s can
    be segmented into a space-separated sequence of one or more dictionary
    words.

    Note that the same word in the dictionary may be reused multiple times in
    the segmentation.

    Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

    Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented
    as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

    Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(maxsize=None)
        def fn(i):
            """Return True if s[i:] can be segmented"""
            if i == len(s):
                return True
            return any(
                s[i : i + len(word)] == word and fn(i + len(word)) for word in wordDict
            )

        return fn(0)

    """# - Combination Sum -
    # https://leetcode.com/problems/combination-sum-iv/
    Given an integer array with all positive numbers and no duplicates, find
    the number of possible combinations that add up to a positive integer
    target.

    Example:
    nums = [1, 2, 3]
    target = 4
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    Note that different sequences are counted as different combinations.
    Therefore the output is 7.

    Follow up:
    * What if negative numbers are allowed in the given array?
    * How does it change the problem?
    * What limitation we need to add to the question to allow negative numbers?
    """

    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def fn(target):
            """Return number of combinations summing up to target."""
            if target <= 0:
                return int(target == 0)
            return sum(fn(target - num) for num in nums)

        return fn(target)

    """# - House Robber -
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

    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def fn(i):
            """Return the maximum amount of money after robbing ith house"""
            if i < 0:
                return 0
            return max(fn(i - 1), fn(i - 2) + nums[i])

        return fn(len(nums) - 1)

    """# - House Robber II -
    # https://leetcode.com/problems/house-robber-ii/
    You are a professional robber planning to rob houses along a street. Each
    house has a certain amount of money stashed. All houses at this place are
    arranged in a circle. That means the first house is the neighbor of the
    last one. Meanwhile, adjacent houses have security system connected and it
    will automatically contact the police if two adjacent houses were broken
    into on the same night. Given a list of non-negative integers representing
    the amount of money of each house, determine the maximum amount of money
    you can rob tonight without alerting the police.

    Example 1:
    Input: [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3
    (money = 2), because they are adjacent houses.

    Example 2:
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4."""

    def rob_(self, nums: List[int]) -> int:
        if len(nums) == 1:  # edge case
            return nums[0]

        def fn(lo, hi):
            """Return money after robbing houses[lo:hi]"""
            f0 = f1 = 0
            for i in range(lo, hi):
                f0, f1 = f1, max(f1, f0 + nums[i])
            return f1

        return max(fn(0, len(nums) - 1), fn(1, len(nums)))

    """# - Decode Ways -
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

    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def fn(i):
            """Return decode ways of s[i:]"""
            if i >= len(s):
                return i == len(s)
            return (
                0 if s[i] == "0" else fn(i + 1) + (int(s[i : i + 2]) <= 26) * fn(i + 2)
            )

        return fn(0)

    """# - Unique Paths -
    # https://leetcode.com/problems/unique-paths/
    There is a robot on an m x n grid. The robot is initially located at the top-left
    corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
    (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any
    point in time.

    Given the two integers m and n, return the number of possible unique paths that the
    robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or equal to 2*109.

    Example 1:
    R ▢ ▢ ▢ ▢ ▢ ▢
    ▢ ▢ ▢ ▢ ▢ ▢ ▢
    ▢ ▢ ▢ ▢ ▢ ▢ S
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

    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)

    def uniquePaths_(self, m: int, n: int) -> int:
        def choose(n, k):
            """Return n choose k"""
            ans, k = 1, min(k, n - k)
            for i in range(k):
                ans *= n - i
                ans //= i + 1
            return ans

        return choose(m + n - 2, m - 1)

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

    def canJump(self, nums: List[int]) -> bool:
        limit = 0
        for i in range(len(nums)):
            if i > limit:
                return False
            limit = max(limit, i + nums[i])
        return True


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List[Node]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Graph:
    """
    # - Clone Graph -
    # https://leetcode.com/problems/clone-graph/
    Given a reference of a node in a connected undirected graph.
    Return a deep copy (clone) of the graph.
    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

    class Node {
        public int val;
        public List<Node> neighbors;
    }

    Test case format:
    For simplicity, each node's value is the same as the node's index (1-indexed). For
    example, the first node with val == 1, the second node with val == 2, and so on.
    The graph is represented in the test case using an adjacency list.

    An adjacency list is a collection of unordered lists used to represent a finite
    graph. Each list describes the set of neighbors of a node in the graph.

    The given node will always be the first node with val = 1. You must return the
    copy of the given node as a reference to the cloned graph.

    Example 1:
    1 - 2
    |   |
    4 - 3
    # NOTE can't be same objects at nodes
    # NOTE can't mess up the connections
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

    Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of
    only one node with val = 1 and it does not have any neighbors.

    Example 3:
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.
    """

    def cloneGraph(self, node: Node) -> Node:
        memo: Dict[Node, Node] = {}

        def fn(n: Node) -> Node:
            if n not in memo:
                clone = memo[n] = Node(n.val)
                clone.neighbors = [fn(nn) for nn in n.neighbors]
            return memo[n]

        return node and fn(node)

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
    # FIXME fix type hints
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        graph = {}  # type:ignore
        for course, prereq in prerequisites:
            indeg[course] += 1
            graph.setdefault(prereq, []).append(course)

        stack = [i for i, x in enumerate(indeg) if x == 0]
        seen = []  # type:ignore
        while stack:
            x = stack.pop()
            seen.append(x)
            for xx in graph.get(x, []):
                indeg[xx] -= 1
                if indeg[xx] == 0:
                    stack.append(xx)
        return len(seen) == numCourses

    """
    # - Pacific Atlantic Water Flow -
    # https://leetcode.com/problems/pacific-atlantic-water-flow/
    There is an m x n rectangular island that borders both the Pacific Ocean
    and Atlantic Ocean. The Pacific Ocean touches the island's left and top
    edges, and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an
    m x n integer matrix heights where heights[r][c] represents the height
    above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring
    cells directly north, south, east, and west if the neighboring cell's height
    is less than or equal to the current cell's height. Water can flow from any
    cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that
    rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

           Pacific
    P   1  2  2  3 _5  A
    a   3  2  3 _4 _4  t
    c   2  4 _5  3  1  l
    i  _6 _7  1  4  5  a
    f  _5  1  1  2  4  n
    i      Atlantic    t
    c                  i
                       c
    Example 1:
    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    Example 2:
    Input: heights = [[2,1],[1,2]]
    Output: [[0,0],[0,1],[1,0],[1,1]]
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # O(rows * cols) time and space
        if not heights or not heights[0]:
            return []

        len_cols, len_rows = len(heights[0]), len(heights)

        def bfs(starts) -> Set[Tuple[int, int]]:
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]:
                    if (
                        0 <= dx < len_rows
                        and 0 <= dy < len_cols
                        and (dx, dy) not in visited
                        and heights[dx][dy] >= heights[x][y]
                    ):
                        queue.append((dx, dy))
                        visited.add((dx, dy))
            return visited

        pacific = [(0, i) for i in range(len_cols)] + [
            (i, 0) for i in range(1, len_rows)
        ]  # top and left edges
        atlantic = [(len_rows - 1, i) for i in range(len_cols)] + [
            (i, len_cols - 1) for i in range(len_rows - 1)
        ]  # bottom and right edges

        return [list(pair) for pair in (bfs(pacific) & bfs(atlantic))]

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
        # DFS O(mn) time and space, m = rows, n = cols
        def fn(i, j, grid: List[List[str]]) -> None:
            """DFS, flood island with `0`s."""
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
    """
    # - Alien Dictionary (Leetcode Premium) -
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

    def alienOrder(self, words: List[str]) -> str:
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)  # type:ignore
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)


class UnionFind:
    def __init__(self, n: int):
        # O(n) space
        self.parent = [node for node in range(n)]
        self.size = [1] * n

    def find(self, A: int) -> int:
        # O(inverse Ackermann function) time
        while self.parent[A] != A:
            A, self.parent[A] = self.parent[A], self.parent[self.parent[A]]
        return A

    def union(self, A: int, B: int) -> bool:
        """True if a merge happened, False otherwise"""
        # O(inverse Ackermann function) time
        root_A = self.find(A)
        root_B = self.find(B)

        if root_A == root_B:
            return False

        if self.size[root_A] < self.size[root_B]:
            root_A, root_B = root_B, root_A

        self.parent[root_B] = root_A
        self.size[root_A] += self.size[root_B]
        return True


class GraphUnion:
    """
    # - Graph Valid Tree (Leetcode Premium) -
    # https://leetcode.com/problems/graph-valid-tree/
    You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an
    integer `n` and a list of edges where `edges[i] = [ai, bi]` indicates that there
    is an undirected edge between nodes `ai` and `bi` in the graph.

    Return `true` if the edges of the given graph make up a valid tree, and
    `false` otherwise.

    Example 1:
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true

    Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false
    """

    """
    Recall that a graph, G, is a tree iff the following two conditions are met:
        - G is fully connected. In other words, for every pair of nodes in G, there is
        a path between them.
        - G contains no cycles. In other words, there is exactly one path between each
        pair of nodes in G.
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS, O(n) time, O(n) space
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]  # type:ignore
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = {0}  # only to protect against cycles
        queue: Deque[int] = deque([0])

        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                queue.append(neighbour)

        return len(seen) == n

    def validTree_(self, n: int, edges: List[List[int]]) -> bool:
        # O(N * inverse Ackermann function) time, O(N) space

        if len(edges) != n - 1:
            return False

        unionFind = UnionFind(n)
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        return True

    """
    # - Number of Connected Components in an Undirected Graph (Leetcode Premium) -
    # https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
    You have a graph of n nodes. You are given an integer n and an array edges where
    edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

    Return the number of connected components in the graph.

    Example 1:
    0 - 1 3
        | |
        2 4
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

    Example 2:
    0 - 1 3
        |/|
        2 4
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1
    """

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # O(N * inverse Ackermann function) time, O(N) space
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])

        parent = set()
        for i in range(n):
            parent.add(uf.find(i))
        return len(parent)


class Interval:
    """
    # - Non-overlapping Intervals -
    # https://leetcode.com/problems/non-overlapping-intervals/
    Given an array of intervals intervals where intervals[i] = [starti, endi],
    return the minimum number of intervals you need to remove to make the rest
    of the intervals non-overlapping.

    Example 1:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals
    are non-overlapping.

    Example 2:
    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals
    non-overlapping.

    Example 3:
    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're
    already non-overlapping.
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(nlogn) time O(1) space
        ans, prev = 0, -inf
        for x, y in sorted(intervals, key=lambda x: x[1]):
            if x < prev:
                ans += 1
            else:
                prev = y
        return ans

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
            while ans and x <= ans[-1][1]:
                x = min(x, ans.pop()[0])
            ans.append([x, y])
        return ans

    """
    # - Insert Interval -
    # https://leetcode.com/problems/insert-interval/
    You are given an array of non-overlapping intervals intervals where intervals[i] =
    [starti, endi] represent the start and the end of the ith interval and intervals is
    sorted in ascending order by starti. You are also given an interval newInterval =
    [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending
    order by starti and intervals still does not have any overlapping intervals
    (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
    """

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans: List[List[int]] = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:  # old: [1,2] new: [3,4]
                ans.append(interval)
            elif interval[0] <= newInterval[1]:  # old: [2 3] new: [2 5]
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else:  # old: [5 6] new: [3 4]
                ans.append(newInterval)
                return ans + intervals[i:]
        return ans + [newInterval]

    """
    # - Meeting Rooms (Leetcode Premium) -
    # https://leetcode.com/problems/meeting-rooms/
    Given an array of meeting time intervals where intervals[i] = [starti, endi],
    determine if a person could attend all meetings.

    Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false

    Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: true
    """

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(
            intervals[i - 1][1] <= intervals[i][0] for i in range(1, len(intervals))
        )

    def canAttendMeetings_(self, intervals: List[List[int]]) -> bool:
        # O(nlogn) time, O(1) space
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True

    """
    # - Meeting Rooms II (Leetcode Premium) -
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
        # O(nlogn) time, O(n) space
        if not intervals:
            return 0
        free_rooms = []  # type:ignore
        intervals.sort(key=lambda x: x[0])
        heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heappop(free_rooms)
            heappush(free_rooms, i[1])
        return len(free_rooms)


class ListNode:
    """LinkedList helper"""

    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class LinkedList:
    """
    # - Reverse a Linked List - https://leetcode.com/problems/reverse-linked-list/
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:
    (1) -> (2) -> (3) -> (4) -> (5)
                |
                V
    (5) -> (4) -> (3) -> (2) -> (1)

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Example 2:
    (1) -> (2)
        |
        V
    (2) -> (1)

    Input: head = [1,2]
    Output: [2,1]

    Example 3:
    Input: head = []
    Output: [] # return None
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node = None, head
        while node:
            node.next, node, prev = prev, node.next, node
        return prev

    """
    # - Detect Cycle in a Linked List -
    # https://leetcode.com/problems/linked-list-cycle/
    Given head, the head of a linked list, determine if the linked list has a cycle
    in it.

    There is a cycle in a linked list if there is some node in the list that can be
    reached again by continuously following the next pointer. Internally, pos is used
    to denote the index of the node that tail's next pointer is connected to. Note that
    pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    Example 1:
    (3) -> (2) -> (0) -> (-4) ┐
            ^                 |
            |_________________|

    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the
    1st node (0-indexed).

    Example 2:
    (1) -> (2) ┐
     ^         |
     |_________|

    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the
    0th node.

    Example 3:
    (1)

    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next  # type:ignore
            slow = slow.next  # type: ignore
            if fast == slow:
                return True
        return False

    """
    # - Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/
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

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            node.next = list1
            list1, node = list1.next, node.next
        node.next = list1 or list2
        return dummy.next

    """
    # - Merge K Sorted Lists -
    # https://leetcode.com/problems/merge-k-sorted-lists/
    You are given an array of k linked-lists lists, each linked-list is sorted
    in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Example 1:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

    Example 2:

    Input: lists = []
    Output: []

    Example 3:

    Input: lists = [[]]
    Output: []
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [(x.val, i, x) for i, x in enumerate(lists) if x]
        heapify(pq)
        dummy = node = ListNode()

        while pq:
            _, i, x = heappop(pq)
            node.next = node = x
            if x.next:
                heappush(pq, (x.next.val, i, x.next))
        return dummy.next

    """
    # - Remove Nth Node From End Of List -
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    Given the head of a linked list, remove the nth node from the end of the list
    and return its head.

    Example 1:
    (1) -> (2) -> (3) -> (4) -> (5)
                   |
                   v
    (1) -> (2) -> (3) --------> (5)

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

    Example 2:

    Input: head = [1], n = 1
    Output: []

    Example 3:

    Input: head = [1,2], n = 1
    Output: [1]
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = slow = dummy
        i = 0
        while fast:
            fast = fast.next  # type:ignore
            if (i := i + 1) > n + 1:
                slow = slow.next  # type: ignore
        slow.next = slow.next.next  # type: ignore
        return dummy.next

    """
    # - Reorder List -
    # https://leetcode.com/problems/reorder-list/
    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
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

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next  # type:ignore

        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next  # type:ignore

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:  # type: ignore
            first.next, first = second, first.next  # type: ignore
            second.next, second = first, second.next  # type: ignore


class Matrix:
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

    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(mn) time, O(1) space
        num_cols, num_rows = len(matrix[0]), len(matrix)
        r1 = any(matrix[0][j] == 0 for j in range(num_cols))
        c1 = any(matrix[i][0] == 0 for i in range(num_rows))
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[i][0] * matrix[0][j] == 0:
                    matrix[i][j] = 0

        if r1:
            for i in range(num_cols):
                matrix[0][i] = 0

        if c1:
            for j in range(num_rows):
                matrix[j][0] = 0

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

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans: List[int] = []
        i = j = 0
        di, dj = 0, 1
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None  # type:ignore
            if not (
                0 <= i + di < m
                and 0 <= j + dj < n
                and matrix[i + di][j + dj] is not None
            ):
                di, dj = dj, -di  # rotate clockwise (di, dj = -dj, di for CCW)
            i += di
            j += dj
        return ans

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

    # def rotate(self, matrix: List[List[int]]) -> None:
    # matrix[:] = list(zip(*matrix[::-1]))

    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = list(list(row) for row in zip(*matrix[::-1]))

    class rotate_:
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

    def exist(self, board: List[List[str]], word: str) -> bool:
        # O(m*n*3^k) time, O(k) space
        def dfs(index, i, j):
            nonlocal found
            if found:
                return

            if index == k:
                found = True
                return

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            temp = board[i][j]
            if temp != word[index]:
                return

            board[i][j] = None  # type:ignore
            for x, y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                dfs(index + 1, i + x, j + y)
            board[i][j] = temp

        found = False
        m, n, k = len(board), len(board[0]), len(word)

        for i, j in product(range(m), range(n)):
            if found:
                return True
            dfs(0, i, j)
        return found


class String:
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
            c = s[j]
            if c in mp:
                i = max(mp[c] + 1, i)
            ans = max(ans, j - i + 1)
            mp[c] = j
        return ans

    """
    # - Longest Repeating Character Replacement -
    # https://leetcode.com/problems/longest-repeating-character-replacement/
    You are given a string s and an integer k. You can choose any character of
    the string and change it to any other uppercase English character. You can
    perform this operation at most k times.

    Return the length of the longest substring containing the same letter you
    can get after performing the above operations.

    Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

    Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    """

    def characterReplacement(self, s: str, k: int) -> int:
        # TODO I honestly still don't get it 100% need to revisit
        maxf = i = 0
        count: Dict[str, int] = Counter()
        for j in range(len(s)):
            ic, jc = s[i], s[j]
            count[jc] += 1
            maxf = max(maxf, count[jc])
            if j - i + 1 > maxf + k:
                count[ic] -= 1
                i += 1
        return len(s) - i

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

    def minWindow(self, s: str, t: str) -> str:
        # TODO revisit, hard
        # NOTE missing optimization
        if not t or not s:
            return ""
        freq_t: Dict[str, int] = Counter(t)
        full_count, required = 0, len(freq_t)
        l, r = 0, 0
        window_counts: Dict[str, int] = {}  # unique chars counts in current window
        ans = inf, None, None  # (window length, left, right)
        while r < len(s):
            char_r = s[r]
            window_counts[char_r] = window_counts.get(char_r, 0) + 1
            if char_r in freq_t and window_counts[char_r] == freq_t[char_r]:
                full_count += 1
            while l <= r and full_count == required:
                char_l = s[l]
                if r - l + 1 < ans[0]:
                    # smallest window
                    ans = (r - l + 1, l, r)  # type: ignore
                window_counts[char_l] -= 1
                if char_l in freq_t and window_counts[char_l] < freq_t[char_l]:
                    full_count -= 1
                l += 1
            r += 1
        return "" if ans[0] == inf else s[ans[1] : ans[2] + 1]  # type: ignore

    def minWindow_(self, s: str, t: str) -> str:
        freq = Counter(t)

        count = ii = jj = 0
        queue: Deque[Tuple[int, str]] = deque()
        ts: Set[str] = set(t)
        for j, c in enumerate(s):
            if c in ts:
                queue.append((j, c))
                freq[c] -= 1
                if freq[c] == 0:
                    count += 1  # enough c in s
                while count == len(ts):
                    i, c = queue.popleft()
                    if not jj or j - i < jj - ii:
                        ii, jj = i, j + 1
                    if freq[c] == 0:
                        count -= 1  # not enough c in s
                    freq[c] += 1
        return s[ii:jj]

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

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: Dict[str, List[str]] = {}
        for word in strs:
            d.setdefault("".join(sorted(word)), []).append(word)
        return list(d.values())

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
        match, stack = {"(": ")", "[": "]", "{": "}"}, []
        for x in s:
            if x in match:
                stack.append(x)
            elif not stack or match[stack.pop()] != x:
                return False
        return not stack

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

    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s.lower() if c.isalnum())
        return s == s[::-1]

    def isPalindrome_(self, s: str) -> bool:
        t = re.sub(r"[\W_]+", "", s).upper()
        return t == t[::-1]

    """
    # - Longest Palindromic Substring -
    # https://leetcode.com/problems/longest-palindromic-substring/
    Given a string s, return the longest palindromic substring in s.

    Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

    Example 2:
    Input: s = "cbbd"
    Output: "bb"
    """

    def longestPalindrome(self, s: str) -> str:
        def helper(i: int, j: int) -> str:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i + 1 : j]

        ans = ""
        for k in range(len(s)):
            ans = max(helper(k, k), helper(k, k + 1), ans, key=len)
        return ans

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

    def countSubstrings(self, s: str) -> int:
        n: Final = len(s)
        dp = [[0] * n for _ in range(n)]

        ans = 0
        for i in reversed(range(n)):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j - i + 1) < 3 or dp[i + 1][j - 1])
                ans += dp[i][j]
        return ans

    """
    # - Encode and Decode Strings (Leetcode Premium) -
    # https://leetcode.com/problems/encode-and-decode-strings/
    Design an algorithm to encode a list of strings to a string. The encoded string is
    then sent over the network and is decoded back to the original list of strings.

    Machine 1 (sender) has the function:

    string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
    }
    Machine 2 (receiver) has the function:
    vector<string> decode(string s) {
    //... your code
    return strs;
    }
    So Machine 1 does:

    string encoded_string = encode(strs);
    and Machine 2 does:

    vector<string> strs2 = decode(encoded_string);
    strs2 in Machine 2 should be the same as strs in Machine 1.

    Implement the encode and decode methods.

    You are not allowed to solve the problem using any serialize methods (such as eval).

    Example 1:
    Input: dummy_input = ["Hello","World"]
    Output: ["Hello","World"]

    Explanation:
    Machine 1:
    Codec encoder = new Codec();
    String msg = encoder.encode(strs);
    Machine 1 ---msg---> Machine 2
    Machine 2:
    Codec decoder = new Codec();
    String[] strs = decoder.decode(msg);

    Example 2:
    Input: dummy_input = [""]
    Output: [""]

    NOTE strs[i] contains any possible characters out of 256 valid ASCII characters.
    """

    class Codec:
        # simple non ascii solution
        def encode(self, strs: List[str]) -> str:
            # O(n) time, O(1) space
            if len(strs) == 0:
                return chr(258)
            return chr(257).join(str_ for str_ in strs)

        def decode(self, s: str) -> List[str]:
            # O(n) time, O(n) space
            if s == chr(258):
                return []
            return s.split(chr(257))

    class Codec_:
        # chuncked transfer encoding
        # eg "4|abcd3|efg"
        def encode(self, strs: List[str]) -> str:
            # O(n) time, O(1) space
            return "".join(f"{len(ss)}|{ss}" for ss in strs)

        def decode(self, s: str) -> List[str]:
            # O(n) time, O(n) space
            ans = []
            i = 0
            while i < len(s):
                ii = s.find("|", i)
                i = ii + int(s[i:ii]) + 1
                ans.append(s[ii + 1 : i])
            return ans

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
    # NOTE levenshtein distance, not in original 75 list
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @lru_cache(maxsize=None)
        def fn(i, j):
            """Return edit distance between word1[i:] and word2[j:]"""
            if i == m or j == n:
                return m + n - i - j
            if word1[i] == word2[j]:
                return fn(i + 1, j + 1)
            return 1 + min(fn(i + 1, j), fn(i, j + 1), fn(i + 1, j + 1))

        return fn(0, 0)


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


TrieNodeType = Dict[str, "TrieNodeType"]  # type:ignore
TrieNode: Callable[[], TrieNodeType] = lambda: defaultdict(TrieNode)


class TrieNode_:
    def __init__(self):
        self.word = False
        self.children = {}


class Tree:
    r"""
    # - Maximum Depth of Binary Tree -
    # https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest
    path from the root node down to the farthest leaf node.

    Example 1:
        (3)
       /   \
    (9)   (20)
          /  \
        (15) (7)
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Example 2:
    Input: root = [1,null,2]
    Output: 2
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def fn(node):
            if not node:
                return 0
            return 1 + max(fn(node.left), fn(node.right))

        return fn(root)

    r"""
    # - Same Tree -
    # https://leetcode.com/problems/same-tree/
    Given the roots of two binary trees p and q, write a function to check if
    they are the same or not.

    Two binary trees are considered the same if they are structurally
    identical, and the nodes have the same value.

    Example 1:
        (1)             (1)
       /   \           /   \
    (2)    (3)       (2)   (3)
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

    Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def fn(p, q):
            if not p or not q:
                return p is q
            return fn(p.left, q.left) and p.val == q.val and fn(p.right, q.right)

        return fn(p, q)

    r"""
    # - Invert/Flip Binary Tree -
    # https://leetcode.com/problems/invert-binary-tree/
    Given the root of a binary tree, invert the tree, and return its root.

    Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    Example 2:
        (2)                 (2)
        / \        ->       / \
     (1)   (3)           (3)   (1)
    Input: root = [2,1,3]
    Output: [2,3,1]

    Example 3:
    Input: root = []
    Output: []
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

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

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_gain(node):
            nonlocal ans
            if not node:
                return 0
            lgain, rgain = max(max_gain(node.left), 0), max(max_gain(node.right), 0)
            new_path = node.val + lgain + rgain
            ans = max(ans, new_path)
            return node.val + max(lgain, rgain)

        ans = -inf
        max_gain(root)
        return ans  # type: ignore

    def maxPathSum_(self, root: Optional[TreeNode]) -> int:
        def fn(node):
            if not node:
                return 0, -inf
            lh, lps = fn(node.left)
            rh, rps = fn(node.right)
            return node.val + max(0, lh, rh), max(
                lps, rps, node.val + max(0, lh) + max(0, rh)
            )

        return fn(root)[1]  # type: ignore

    r"""
    # - Binary Tree Level Order Traversal -
    # https://leetcode.com/problems/binary-tree-level-order-traversal/
    Given the root of a binary tree, return the level order traversal of
    its nodes' values. (i.e., from left to right, level by level).

    Example 1:
        (3)
        / \
     (9)  (20)
          /  \
        (15) (7)
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Example 2:
    Input: root = [1]
    Output: [[1]]

    Example 3:
    Input: root = []
    Output: []
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, queue = [], [root]
        while queue:
            newq, vals = [], []
            for node in queue:
                if node:
                    vals.append(node.val)
                    newq.extend([node.left, node.right])
            if vals:
                ans.append(vals)
            queue = newq
        return ans

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

    class Codec:
        """DFS O(n) time O(n) space"""

        def serialize(self, root: Optional[TreeNode]) -> str:
            def rserialize(root, string):
                if root is None:
                    string += "None,"
                else:
                    string += str(root.val) + ","
                    string = rserialize(root.left, string)
                    string = rserialize(root.right, string)
                return string

            return rserialize(root, "")

        def deserialize(self, data: str) -> Optional[TreeNode]:
            def rdeserialize(l):
                if l[0] == "None":
                    l.pop(0)
                    return None

                root = TreeNode(l[0])
                l.pop(0)
                root.left = rdeserialize(l)
                root.right = rdeserialize(l)
                return root

            data_list = data.split(",")
            root = rdeserialize(data_list)
            return root

    class Codec_:
        r""" BFS O(n) time and O(n) space, BFS traversal
        e.g., 1
             / \
           2    5
         / \
        3   4  , level order traversal, serialize will be '1,2,5,3,4,None,None,None,None,None,None,'; deserialize
        with queue as well, convert back. Time and Space O(n).
        """

        def serialize(self, root: Optional[TreeNode]) -> str:
            if not root:
                return ""
            queue: Deque[TreeNode] = deque()
            queue.append(root)
            ans = ""
            while queue:
                node = queue.popleft()
                if not node:
                    ans += "None,"
                    continue
                ans += str(node.val) + ","
                queue.append(node.left)  # type: ignore
                queue.append(node.right)  # type: ignore
            return ans

        def deserialize(self, data: str) -> Optional[TreeNode]:
            if not data:
                return None
            ls: Final = data.split(",")
            root = TreeNode(int(ls[0]))
            queue: Deque[TreeNode] = deque()
            queue.append(root)
            i = 1
            while queue and i < len(ls):
                node = queue.popleft()
                if ls[i] != "None":
                    left = TreeNode(int(ls[i]))
                    node.left = left
                    queue.append(left)
                i += 1
                if ls[i] != "None":
                    right = TreeNode(int(ls[i]))
                    node.right = right
                    queue.append(right)
                i += 1
            return root

    r"""
    # - Subtree of Another Tree -
    # https://leetcode.com/problems/subtree-of-another-tree/
    Given the roots of two binary trees `root` and `subRoot`, return `true` if there
    is a subtree of `root` with the same structure and node values of `subRoot`
    and `false` otherwise.

    A subtree of a binary tree `tree` is a tree that consists of a node in `tree`
    and all of this node's descendants. The tree `tree` could also be considered
    as a subtree of itself.

    Example 1:
        3         4
       / \       / \
      4   5     1   2
     / \
    1   2
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

    Example 2:
    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)

        if not root:
            return False
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    """
    # - Construct Binary Tree from Preorder and Inorder Traversal -
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    Given two integer arrays preorder and inorder where preorder is the preorder
    traversal of a binary tree and inorder is the inorder traversal of the same
    tree, construct and return the binary tree.

    Example 1:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

    Example 2:
    Input: preorder = [-1], inorder = [-1]
    Output: [-1]
    # NOTE no duplicates in tree
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index + 1 :])
            return root
        return None

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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def fn(root, floor=float("-inf"), ceiling=float("inf")):
            if not root:
                return True
            if root.val <= floor or root.val >= ceiling:
                return False
            # in the left branch, root is the new ceiling;
            # contrarily root is the new floor in right branch
            return fn(root.left, floor, root.val) and fn(root.right, root.val, ceiling)

        return fn(root)

    def isValidBST_(self, root: Optional[TreeNode]) -> bool:
        def fn(node, lo=-inf, hi=inf):
            if not node:
                return True
            return (
                fn(node.left, lo, node.val)
                and lo < node.val < hi
                and fn(node.right, node.val, hi)
            )

        return fn(root)

    r"""
    # - Kth Smallest Element in a BST -
    # https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    Given the root of a binary search tree, and an integer k, return the kth
    smallest value (1-indexed) of all the values of the nodes in the tree.

    Example 1:
        3
       / \
      1   4
       \
        2
    Input: root = [3,1,4,null,2], k = 1
    Output: 1

    Example 2:
                5
               / \
              3   6
             / \
            2   4
           /
          1
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

    Follow up: If the BST is modified often (i.e., we can do insert and delete
    operations) and you need to find the kth smallest frequently, how would
    you optimize?
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # O(n) time, O(n) space
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]  # nth smallest is nth element of inorder traverse 🤯

    def kthSmallest_(self, root: Optional[TreeNode], k: int) -> int:
        # O(H + k) time, O(H) space
        # NOTE O(log N + k) time for balanced tree, O(N + k) for unbalanced on left
        node = root
        stack: List[TreeNode] = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
                continue
            node = stack.pop()
            if (k := k - 1) == 0:
                return node.val
            node = node.right
        raise Exception

    r"""
    # - Lowest Common Ancestor of BST -
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
    given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is
    defined between two nodes p and q as the lowest node in T that has both p and q as
    descendants (where we allow a node to be a descendant of itself).”

    Example 1:
                 6
               /   \
              2     8
             / \   / \
            0   4 7   9
               / \
              3   5
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

    Example 2:
                 6
               /   \
              2     8
             / \   / \
            0   4 7   9
               / \
              3   5
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of
    itself according to the LCA definition.

    Example 3:
    Input: root = [2,1], p = 2, q = 1
    Output: 2
    """

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:  # type: ignore
        # O(n) time, O(1) space
        node = root
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right  # type:ignore
            elif p.val < node.val and q.val < node.val:
                node = node.left  # type:ignore
            else:
                return node
        raise Exception

    """
    # - Implement Trie (Prefix Tree) -
    # https://leetcode.com/problems/implement-trie-prefix-tree/
    A trie (pronounced as "try") or prefix tree is a tree data structure used to
    efficiently store and retrieve keys in a dataset of strings. There are various
    applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie
    (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously
    inserted string word that has the prefix prefix, and false otherwise.

    Example 1:
    Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
    [null, null, true, false, true, null, true]

    Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True
    """

    class Trie:
        # O(m) time where m is string len, O(1) space
        def __init__(self):
            self.trie = TrieNode()

        def insert(self, word):
            reduce(lambda d, k: d[k], word, self.trie)["end"] = True  # type: ignore

        def search(self, word):
            return reduce(
                lambda d, k: d[k] if k in d else TrieNode(), word, self.trie
            ).get("end", False)

        def startsWith(self, word):
            return bool(
                reduce(
                    lambda d, k: d[k] if k in d else TrieNode(), word, self.trie
                ).keys()
            )

    class Trie_:
        def __init__(self):
            self.root = TrieNode_()

        def insert(self, word: str) -> None:
            node = self.root
            for i in word:
                if i not in node.children:
                    node.children[i] = TrieNode_()
                node = node.children[i]
            node.word = True

        def search(self, word: str) -> bool:
            node = self.root
            for i in word:
                if i not in node.children:
                    return False
                node = node.children[i]
            return node.word

        def startsWith(self, prefix: str) -> bool:
            node = self.root
            for i in prefix:
                if i not in node.children:
                    return False
                node = node.children[i]
            return True

    class Trie__:
        # NOTE all inputs assumed to consist of lowercase letters a-z.
        # NOTE all inputs are guaranteed to be non-empty strings.
        def __init__(self):
            # TODO recursive type pyright
            # Node = Dict[str, "Node"]
            self.root = {}

        def insert(self, word: str) -> None:
            node = self.root
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word

        def search(self, word: str) -> bool:
            node = self.root
            for char in word:
                if char not in node:
                    return False
                node = node[char]
            return bool(node.get("$"))  # TODO this passes without the bool???????

        def startsWith(self, prefix: str) -> bool:
            node = self.root
            for char in prefix:
                if char not in node:
                    return False
                node = node[char]
            return True

    """
    # - Add and Search Word -
    # https://leetcode.com/problems/add-and-search-word-data-structure-design/
    Design a data structure that supports adding new words and finding if a string
    matches any previously added string.

    Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that
    matches word or false otherwise. word may contain dots '.' where dots can be
    matched with any letter.

    Example:
    Input
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output
    [null,null,null,null,false,true,true,true]

    Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True
    """

    class WordDictionary:
        # NOTE slow timeouts sometimes
        def __init__(self):
            self.trie = {}

        def addWord(self, word: str) -> None:
            node = self.trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word

        def search(self, word: str) -> bool:
            def fn(node, i):
                if not node:
                    return False
                if i == len(word):
                    return node.get("$")
                if word[i] == ".":
                    return any(fn(node[k], i + 1) for k in node if k != "$")
                return fn(node.get(word[i]), i + 1)

            return fn(self.trie, 0)

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

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # TODO clean up, lots of solutions time out now on new tests
        WORD_KEY = "$"

        trie = {}  # type:ignore
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = "#"

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords


class Heap:
    """
    # - Top K Frequent Elements -
    # https://leetcode.com/problems/top-k-frequent-elements/
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:
    Input: nums = [1], k = 1
    Output: [1]
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Bucket sort O(n) time, O(n) space"""
        bucket: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums).items()
        for num, freq in count:
            # freq can't be bigger than len(nums)
            bucket[freq].append(num)
        arr = list(chain(*bucket))
        return arr[::-1][:k]

    def topKFrequent_(self, nums: List[int], k: int) -> List[int]:
        """Heapq way, O(nlogn) or nlogk time, O(n) space"""
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return nlargest(k, count.keys(), key=count.__getitem__)

    def topKFrequent__(self, nums: List[int], k: int) -> List[int]:
        """Calls heapq under the hood"""
        return [x for x, y in Counter(nums).most_common(k)]

    class MedianFinder:
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

        def __init__(self):
            ...

        def addNum(self, num: int) -> None:
            ...

        def findMedian(self) -> float:
            ...
