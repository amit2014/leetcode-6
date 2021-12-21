from typing import List, Tuple
from math import inf

class Array:
    """
     - Two Sum - https://leetcode.com/problems/two-sum/
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

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


    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """O(n) time, O(n) space"""
        seen = dict()
        for i, x in enumerate(nums):
            if target - x in seen: return [seen[target - x], i]
            seen[x] = i

    """
    # - Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
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
        buy, profit = inf, 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit


    """
    # - Contains Duplicate - https://leetcode.com/problems/contains-duplicate/
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



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
    # - Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.



    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]


    Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


    Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
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
    # - Maximum Subarray - https://leetcode.com/problems/maximum-subarray/
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

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


    Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        """O(n) time, O(1) space"""
        cur = ans = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            ans = max(ans, cur)
        return ans


# - Maximum Product Subarray - https://leetcode.com/problems/maximum-product-subarray/
# - Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# - Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/
# - 3Sum - https://leetcode.com/problems/3sum/
# - Container With Most Water - https://leetcode.com/problems/container-with-most-water/

# Binary

# - Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/
# - Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/
# - Counting Bits - https://leetcode.com/problems/counting-bits/
# - Missing Number - https://leetcode.com/problems/missing-number/
# - Reverse Bits - https://leetcode.com/problems/reverse-bits/


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
