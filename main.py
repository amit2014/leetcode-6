from typing import Dict, List


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

    Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


    Follow-up: Can you come up with an algorithm that is less than O(n2) time
    complexity?
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

    Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104
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

    Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
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

    Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a
    32-bit integer.

    Follow up: Can you solve the problem in O(1) extra space complexity? (The
    output array does not count as extra space for space complexity analysis.)
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

    Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

    Follow up: If you have figured out the O(n) solution, try coding another
    solution using the divide and conquer approach, which is more subtle.
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

    Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a
    32-bit integer.
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

    Constraints:

    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times."""

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

    Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104"""

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


    Constraints:

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105"""

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

    Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104"""

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

    Constraints:

    -1000 <= a, b <= 1000"""

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
    Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

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
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
    Example 2:

    Input: n = 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
    Example 3:

    Input: n = 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

    Constraints:

    The input must be a binary string of length 32.

    Follow up: If this function is called many times, how would you optimize it?"""

    def hammingWeight(self, n: int) -> int:
        """O(1)* time, O(1) space *for fixed 32 bit input"""
        return bin(n).count("1")

    def _hammingWeight(self, n: int) -> int:
        """O(1)* time, O(1) space *for fixed 32 bit input)"""
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

    """# - Counting Bits -
    # https://leetcode.com/problems/counting-bits/
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary
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

    def reverseBits(self, n):
        """32 loops solution O(1) time, O(1) space"""
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

    def reverseBits(self, n: int) -> int:
        """no loop solution O(1) time, O(1) space"""
        """
        >>> bin(0xaaaaaaaa)[2:].zfill(32)
        '10101010101010101010101010101010'
        >>> bin(0x55555555)[2:].zfill(32)
        '01010101010101010101010101010101'
        >>> bin(0xcccccccc)[2:].zfill(32)
        '11001100110011001100110011001100'
        >>> bin(0x33333333)[2:].zfill(32)
        '00110011001100110011001100110011'
        >>> bin(0xf0f0f0f0)[2:].zfill(32)
        '11110000111100001111000011110000'
        >>> bin(0x0f0f0f0f)[2:].zfill(32)
        '00001111000011110000111100001111'
        >>> bin(0xff00ff00)[2:].zfill(32)
        '11111111000000001111111100000000'
        >>> bin(0x00ff00ff)[2:].zfill(32)
        '00000000111111110000000011111111'
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

# Dynamic Programming

# - Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
# - Coin Change - https://leetcode.com/problems/coin-change/
# - Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/
# - Longest Common Subsequence -
# - Word Break Problem - https://leetcode.com/problems/word-break/
# - Combination Sum - https://leetcode.com/problems/combination-sum-iv/
# - House Robber - https://leetcode.com/problems/house-robber/
# - House Robber II - https://leetcode.com/problems/house-robber-ii/
# - Decode Ways - https://leetcode.com/problems/decode-ways/
# - Unique Paths - https://leetcode.com/problems/unique-paths/
# - Jump Game - https://leetcode.com/problems/jump-game/


# Graph

# - Clone Graph - https://leetcode.com/problems/clone-graph/
# - Course Schedule - https://leetcode.com/problems/course-schedule/
# - Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow/
# - Number of Islands - https://leetcode.com/problems/number-of-islands/
# - Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/
# - Alien Dictionary (Leetcode Premium) - https://leetcode.com/problems/alien-dictionary/
# - Graph Valid Tree (Leetcode Premium) - https://leetcode.com/problems/graph-valid-tree/
# - Number of Connected Components in an Undirected Graph (Leetcode Premium) - https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


# Interval

# - Insert Interval - https://leetcode.com/problems/insert-interval/
# - Merge Intervals - https://leetcode.com/problems/merge-intervals/
# - Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/
# - Meeting Rooms (Leetcode Premium) - https://leetcode.com/problems/meeting-rooms/
# - Meeting Rooms II (Leetcode Premium) - https://leetcode.com/problems/meeting-rooms-ii/


# Linked List

# - Reverse a Linked List - https://leetcode.com/problems/reverse-linked-list/
# - Detect Cycle in a Linked List - https://leetcode.com/problems/linked-list-cycle/
# - Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/
# - Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
# - Remove Nth Node From End Of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# - Reorder List - https://leetcode.com/problems/reorder-list/


# Matrix

# - Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/
# - Spiral Matrix - https://leetcode.com/problems/spiral-matrix/
# - Rotate Image - https://leetcode.com/problems/rotate-image/
# - Word Search - https://leetcode.com/problems/word-search/

# String

# - Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
# - Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/
# - Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
# - Valid Anagram - https://leetcode.com/problems/valid-anagram/
# - Group Anagrams - https://leetcode.com/problems/group-anagrams/
# - Valid Parentheses - https://leetcode.com/problems/valid-parentheses/
# - Valid Palindrome - https://leetcode.com/problems/valid-palindrome/
# - Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/
# - Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/
# - Encode and Decode Strings (Leetcode Premium) - https://leetcode.com/problems/encode-and-decode-strings/

# Tree

# - Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/
# - Same Tree - https://leetcode.com/problems/same-tree/
# - Invert/Flip Binary Tree - https://leetcode.com/problems/invert-binary-tree/
# - Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/
# - Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/
# - Serialize and Deserialize Binary Tree - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# - Subtree of Another Tree - https://leetcode.com/problems/subtree-of-another-tree/
# - Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# - Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/
# - Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# - Lowest Common Ancestor of BST - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# - Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/
# - Add and Search Word - https://leetcode.com/problems/add-and-search-word-data-structure-design/
# - Word Search II - https://leetcode.com/problems/word-search-ii/

# Heap

# - Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
# - Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/
# - Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/
