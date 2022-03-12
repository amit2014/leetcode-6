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
    ...
class _146:
    """
    # - LRU Cache -
    # https://leetcode.com/problems/lru-cache/
    """
    ...
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
    ...
class _423:
    """
    # - Reconstruct Original Digits from English -
    # https://leetcode.com/problems/reconstruct-original-digits-from-english/
    """
    ...
class _42:
    """
    # - Trapping Rain Water -
    # https://leetcode.com/problems/trapping-rain-water/
    """
    ...
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
    ...
class _4:
    """
    # - Median of Two Sorted Arrays -
    # https://leetcode.com/problems/median-of-two-sorted-arrays/
    """
    ...
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
    ...
class _1249:
    """
    # - Minimum Remove to Make Valid Parentheses -
    # https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
    """
    ...
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
    ...
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
    ...
class _68:
    """
    # - Text Justification -
    # https://leetcode.com/problems/text-justification/
    """
    ...
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
    ...
class _815:
    """
    # - Bus Routes -
    # https://leetcode.com/problems/bus-routes/
    """
    ...
class _588:
    """
    # - Design In-Memory File System -
    # https://leetcode.com/problems/design-in-memory-file-system/
    """
    ...
class _253:
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
    ...
class _680:
    """
    # - Valid Palindrome II -
    # https://leetcode.com/problems/valid-palindrome-ii/
    """
    ...
class _1235:
    """
    # - Maximum Profit in Job Scheduling -
    # https://leetcode.com/problems/maximum-profit-in-job-scheduling/
    """
    ...
class _31:
    """
    # - Next Permutation -
    # https://leetcode.com/problems/next-permutation/
    """
    ...
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
    """
    ...
class _5:
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
    ...
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
    """
    ...
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
    """
    ...
class _394:
    """
    # - Decode String -
    # https://leetcode.com/problems/decode-string/
    """
    ...
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
    """
    ...
class _215:
    """
    # - Kth Largest Element in an Array -
    # https://leetcode.com/problems/kth-largest-element-in-an-array/
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
class _1570:
    """
    # - Dot Product of Two Sparse Vectors -
    # https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
    """
    ...
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
    """
    ...
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
    """
    ...
class _9:
    """
    # - Palindrome Number -
    # https://leetcode.com/problems/palindrome-number/
    """
    ...
class _339:
    """
    # - Nested List Weight Sum -
    # https://leetcode.com/problems/nested-list-weight-sum/
    """
    ...
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
    """
    ...
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
    """
    ...
class _71:
    """
    # - Simplify Path -
    # https://leetcode.com/problems/simplify-path/
    """
    ...
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
    """
    ...
class _347:
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
    ...
class _443:
    """
    # - String Compression -
    # https://leetcode.com/problems/string-compression/
    """
    ...
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
    ...
class _269:
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
class _289:
    """
    # - Game of Life -
    # https://leetcode.com/problems/game-of-life/
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
class _359:
    """
    # - Logger Rate Limiter -
    # https://leetcode.com/problems/logger-rate-limiter/
    """
    ...
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
    """
    ...
class _283:
    """
    # - Move Zeroes -
    # https://leetcode.com/problems/move-zeroes/
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
class _1047:
    """
    # - Remove All Adjacent Duplicates In String -
    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
    """
    ...
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
    """
    ...
class _1015:
    """
    # - Smallest Integer Divisible by K -
    # https://leetcode.com/problems/smallest-integer-divisible-by-k/
    """
    ...
class _155:
    """
    # - Min Stack -
    # https://leetcode.com/problems/min-stack/
    """
    ...
class _202:
    """
    # - Happy Number -
    # https://leetcode.com/problems/happy-number/
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
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
    """
    ...
class _1275:
    """
    # - Find Winner on a Tic Tac Toe Game -
    # https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
    """
    ...
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
