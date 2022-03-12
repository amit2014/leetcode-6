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
    # 
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
    # 
    """
    ...
class _42:
    """
    # - Trapping Rain Water -
    # 
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
    # 
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
    # 
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
    # 
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
    # 
    """
    ...
class _588:
    """
    # - Design In-Memory File System -
    # 
    """
    ...
class _253:
    """
    # - Meeting Rooms II -
    # 
    """
    ...
class _680:
    """
    # - Valid Palindrome II -
    # 
    """
    ...
class _1235:
    """
    # - Maximum Profit in Job Scheduling -
    # 
    """
    ...
class _31:
    """
    # - Next Permutation -
    # 
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
    # 
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
    # 
    """
    ...
class _2:
    """
    # - Add Two Numbers -
    # 
    """
    ...
class _560:
    """
    # - Subarray Sum Equals K -
    # 
    """
    ...
class _811:
    """
    # - Subdomain Visit Count -
    # 
    """
    ...
class _314:
    """
    # - Binary Tree Vertical Order Traversal -
    # 
    """
    ...
class _394:
    """
    # - Decode String -
    # 
    """
    ...
class _1396:
    """
    # - Design Underground System -
    # 
    """
    ...
class _236:
    """
    # - Lowest Common Ancestor of a Binary Tree -
    # 
    """
    ...
class _215:
    """
    # - Kth Largest Element in an Array -
    # 
    """
    ...
class _227:
    """
    # - Basic Calculator II -
    # 
    """
    ...
class _273:
    """
    # - Integer to English Words -
    # 
    """
    ...
class _14:
    """
    # - Longest Common Prefix -
    # 
    """
    ...
class _23:
    """
    # - Merge k Sorted Lists -
    # 
    """
    ...
class _134:
    """
    # - Gas Station -
    # 
    """
    ...
class _973:
    """
    # - K Closest Points to Origin -
    # 
    """
    ...
class _41:
    """
    # - First Missing Positive -
    # 
    """
    ...
class _50:
    """
    # - Pow(x, n) -
    # 
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
    # 
    """
    ...
class _1570:
    """
    # - Dot Product of Two Sparse Vectors -
    # 
    """
    ...
class _828:
    """
    # - Count Unique Characters of All Substrings of a Given String -
    # 
    """
    ...
class _1762:
    """
    # - Buildings With an Ocean View -
    # 
    """
    ...
class _239:
    """
    # - Sliding Window Maximum -
    # 
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
    # 
    """
    ...
class _9:
    """
    # - Palindrome Number -
    # 
    """
    ...
class _339:
    """
    # - Nested List Weight Sum -
    # 
    """
    ...
class _1010:
    """
    # - Pairs of Songs With Total Durations Divisible by 60 -
    # 
    """
    ...
class _696:
    """
    # - Count Binary Substrings -
    # 
    """
    ...
class _17:
    """
    # - Letter Combinations of a Phone Number -
    # 
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
    # 
    """
    ...
class _13:
    """
    # - Roman to Integer -
    # 
    """
    ...
class _938:
    """
    # - Range Sum of BST -
    # 
    """
    ...
class _71:
    """
    # - Simplify Path -
    # 
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
    # 
    """
    ...
class _224:
    """
    # - Basic Calculator -
    # 
    """
    ...
class _7:
    """
    # - Reverse Integer -
    # 
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
    # 
    """
    ...
class _987:
    """
    # - Vertical Order Traversal of a Binary Tree -
    # 
    """
    ...
class _162:
    """
    # - Find Peak Element -
    # 
    """
    ...
class _829:
    """
    # - Consecutive Numbers Sum -
    # 
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
    # 
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
    # - Alien Dictionary -
    # 
    """
    ...
class _1268:
    """
    # - Search Suggestions System -
    # 
    """
    ...
class _210:
    """
    # - Course Schedule II -
    # 
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
    # 
    """
    ...
class _1041:
    """
    # - Robot Bounded In Circle -
    # 
    """
    ...
class _759:
    """
    # - Employee Free Time -
    # 
    """
    ...
class _921:
    """
    # - Minimum Add to Make Parentheses Valid -
    # 
    """
    ...
class _138:
    """
    # - Copy List with Random Pointer -
    # 
    """
    ...
class _1152:
    """
    # - Analyze User Website Visit Pattern -
    # 
    """
    ...
class _362:
    """
    # - Design Hit Counter -
    # 
    """
    ...
class _1326:
    """
    # - Minimum Number of Taps to Open to Water a Garden -
    # 
    """
    ...
class _981:
    """
    # - Time Based Key-Value Store -
    # 
    """
    ...
class _366:
    """
    # - Find Leaves of Binary Tree -
    # 
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
    # 
    """
    ...
class _1197:
    """
    # - Minimum Knight Moves -
    # 
    """
    ...
class _88:
    """
    # - Merge Sorted Array -
    # 
    """
    ...
class _529:
    """
    # - Minesweeper -
    # 
    """
    ...
class _1507:
    """
    # - Reformat Date -
    # 
    """
    ...
class _735:
    """
    # - Asteroid Collision -
    # 
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
    # 
    """
    ...
class _875:
    """
    # - Koko Eating Bananas -
    # 
    """
    ...
class _364:
    """
    # - Nested List Weight Sum II -
    # 
    """
    ...
class _199:
    """
    # - Binary Tree Right Side View -
    # 
    """
    ...
class _1293:
    """
    # - Shortest Path in a Grid with Obstacles Elimination -
    # 
    """
    ...
class _139:
    """
    # - Word Break -
    # 
    """
    ...
class _84:
    """
    # - Largest Rectangle in Histogram -
    # 
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
    # 
    """
    ...
class _198:
    """
    # - House Robber -
    # 
    """
    ...
class _926:
    """
    # - Flip String to Monotone Increasing -
    # 
    """
    ...
class _716:
    """
    # - Max Stack -
    # 
    """
    ...
class _453:
    """
    # - Minimum Moves to Equal Array Elements -
    # 
    """
    ...
class _51:
    """
    # - N-Queens -
    # 
    """
    ...
class _1604:
    """
    # - Alert Using Same Key-Card Three or More Times in a One Hour Period -
    # 
    """
    ...
class _387:
    """
    # - First Unique Character in a String -
    # 
    """
    ...
class _863:
    """
    # - All Nodes Distance K in Binary Tree -
    # 
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
    # 
    """
    ...
class _1048:
    """
    # - Longest String Chain -
    # 
    """
    ...
class _45:
    """
    # - Jump Game II -
    # 
    """
    ...
class _70:
    """
    # - Climbing Stairs -
    # 
    """
    ...
class _415:
    """
    # - Add Strings -
    # 
    """
    ...
class _1209:
    """
    # - Remove All Adjacent Duplicates in String II -
    # 
    """
    ...
class _994:
    """
    # - Rotting Oranges -
    # 
    """
    ...
class _34:
    """
    # - Find First and Last Position of Element in Sorted Array -
    # 
    """
    ...
class _174:
    """
    # - Dungeon Game -
    # 
    """
    ...
class _721:
    """
    # - Accounts Merge -
    # 
    """
    ...
class _1044:
    """
    # - Longest Duplicate Substring -
    # 
    """
    ...
class _509:
    """
    # - Fibonacci Number -
    # 
    """
    ...
class _140:
    """
    # - Word Break II -
    # 
    """
    ...
class _399:
    """
    # - Evaluate Division -
    # 
    """
    ...
class _739:
    """
    # - Daily Temperatures -
    # 
    """
    ...
class _426:
    """
    # - Convert Binary Search Tree to Sorted Doubly Linked List -
    # 
    """
    ...
class _697:
    """
    # - Degree of an Array -
    # 
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
    # 
    """
    ...
class _543:
    """
    # - Diameter of Binary Tree -
    # 
    """
    ...
class _151:
    """
    # - Reverse Words in a String -
    # 
    """
    ...
class _605:
    """
    # - Can Place Flowers -
    # 
    """
    ...
class _525:
    """
    # - Contiguous Array -
    # 
    """
    ...
class _1094:
    """
    # - Car Pooling -
    # 
    """
    ...
class _317:
    """
    # - Shortest Distance from All Buildings -
    # 
    """
    ...
class _1207:
    """
    # - Unique Number of Occurrences -
    # 
    """
    ...
class _25:
    """
    # - Reverse Nodes in k-Group -
    # 
    """
    ...
class _408:
    """
    # - Valid Word Abbreviation -
    # 
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
    # 
    """
    ...
class _1761:
    """
    # - Minimum Degree of a Connected Trio in a Graph -
    # 
    """
    ...
class _1487:
    """
    # - Making File Names Unique -
    # 
    """
    ...
class _871:
    """
    # - Minimum Number of Refueling Stops -
    # 
    """
    ...
class _412:
    """
    # - Fizz Buzz -
    # 
    """
    ...
class _767:
    """
    # - Reorganize String -
    # 
    """
    ...
class _636:
    """
    # - Exclusive Time of Functions -
    # 
    """
    ...
class _370:
    """
    # - Range Addition -
    # 
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
    # 
    """
    ...
class _1091:
    """
    # - Shortest Path in Binary Matrix -
    # 
    """
    ...
class _37:
    """
    # - Sudoku Solver -
    # 
    """
    ...
class _21:
    """
    # - Merge Two Sorted Lists -
    # 
    """
    ...
class _234:
    """
    # - Palindrome Linked List -
    # 
    """
    ...
class _289:
    """
    # - Game of Life -
    # 
    """
    ...
class _1146:
    """
    # - Snapshot Array -
    # 
    """
    ...
class _1291:
    """
    # - Sequential Digits -
    # 
    """
    ...
class _442:
    """
    # - Find All Duplicates in an Array -
    # 
    """
    ...
class _32:
    """
    # - Longest Valid Parentheses -
    # 
    """
    ...
class _790:
    """
    # - Domino and Tromino Tiling -
    # 
    """
    ...
class _465:
    """
    # - Optimal Account Balancing -
    # 
    """
    ...
class _65:
    """
    # - Valid Number -
    # 
    """
    ...
class _438:
    """
    # - Find All Anagrams in a String -
    # 
    """
    ...
class _723:
    """
    # - Candy Crush -
    # 
    """
    ...
class _670:
    """
    # - Maximum Swap -
    # 
    """
    ...
class _878:
    """
    # - Nth Magical Number -
    # 
    """
    ...
class _909:
    """
    # - Snakes and Ladders -
    # 
    """
    ...
class _410:
    """
    # - Split Array Largest Sum -
    # 
    """
    ...
class _421:
    """
    # - Maximum XOR of Two Numbers in an Array -
    # 
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
    # 
    """
    ...
class _827:
    """
    # - Making A Large Island -
    # 
    """
    ...
class _556:
    """
    # - Next Greater Element III -
    # 
    """
    ...
class _1472:
    """
    # - Design Browser History -
    # 
    """
    ...
class _278:
    """
    # - First Bad Version -
    # 
    """
    ...
class _420:
    """
    # - Strong Password Checker -
    # 
    """
    ...
class _1710:
    """
    # - Maximum Units on a Truck -
    # 
    """
    ...
class _150:
    """
    # - Evaluate Reverse Polish Notation -
    # 
    """
    ...
class _332:
    """
    # - Reconstruct Itinerary -
    # 
    """
    ...
class _498:
    """
    # - Diagonal Traverse -
    # 
    """
    ...
class _36:
    """
    # - Valid Sudoku -
    # 
    """
    ...
class _679:
    """
    # - 24 Game -
    # 
    """
    ...
class _780:
    """
    # - Reaching Points -
    # 
    """
    ...
class _329:
    """
    # - Longest Increasing Path in a Matrix -
    # 
    """
    ...
class _103:
    """
    # - Binary Tree Zigzag Level Order Traversal -
    # 
    """
    ...
class _62:
    """
    # - Unique Paths -
    # 
    """
    ...
class _718:
    """
    # - Maximum Length of Repeated Subarray -
    # 
    """
    ...
class _46:
    """
    # - Permutations -
    # 
    """
    ...
class _1861:
    """
    # - Rotating the Box -
    # 
    """
    ...
class _849:
    """
    # - Maximize Distance to Closest Person -
    # 
    """
    ...
class _532:
    """
    # - K-diff Pairs in an Array -
    # 
    """
    ...
class _287:
    """
    # - Find the Duplicate Number -
    # 
    """
    ...
class _44:
    """
    # - Wildcard Matching -
    # 
    """
    ...
class _359:
    """
    # - Logger Rate Limiter -
    # 
    """
    ...
class _189:
    """
    # - Rotate Array -
    # 
    """
    ...
class _706:
    """
    # - Design HashMap -
    # 
    """
    ...
class _283:
    """
    # - Move Zeroes -
    # 
    """
    ...
class _1004:
    """
    # - Max Consecutive Ones III -
    # 
    """
    ...
class _206:
    """
    # - Reverse Linked List -
    # 
    """
    ...
class _935:
    """
    # - Knight Dialer -
    # 
    """
    ...
class _286:
    """
    # - Walls and Gates -
    # 
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
    # 
    """
    ...
class _348:
    """
    # - Design Tic-Tac-Toe -
    # 
    """
    ...
class _907:
    """
    # - Sum of Subarray Minimums -
    # 
    """
    ...
class _1283:
    """
    # - Find the Smallest Divisor Given a Threshold -
    # 
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
    # 
    """
    ...
class _1492:
    """
    # - The kth Factor of n -
    # 
    """
    ...
class _341:
    """
    # - Flatten Nested List Iterator -
    # 
    """
    ...
class _1413:
    """
    # - Minimum Value to Get Positive Step by Step Sum -
    # 
    """
    ...
class _368:
    """
    # - Largest Divisible Subset -
    # 
    """
    ...
class _300:
    """
    # - Longest Increasing Subsequence -
    # 
    """
    ...
class _642:
    """
    # - Design Search Autocomplete System -
    # 
    """
    ...
class _523:
    """
    # - Continuous Subarray Sum -
    # 
    """
    ...
class _353:
    """
    # - Design Snake Game -
    # 
    """
    ...
class _2003:
    """
    # - Smallest Missing Genetic Value in Each Subtree -
    # 
    """
    ...
class _91:
    """
    # - Decode Ways -
    # 
    """
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
    # 
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
    # 
    """
    ...
class _122:
    """
    # - Best Time to Buy and Sell Stock II -
    # 
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
    # 
    """
    ...
class _609:
    """
    # - Find Duplicate File in System -
    # 
    """
    ...
class _809:
    """
    # - Expressive Words -
    # 
    """
    ...
class _726:
    """
    # - Number of Atoms -
    # 
    """
    ...
class _472:
    """
    # - Concatenated Words -
    # 
    """
    ...
class _986:
    """
    # - Interval List Intersections -
    # 
    """
    ...
class _428:
    """
    # - Serialize and Deserialize N-ary Tree -
    # 
    """
    ...
class _127:
    """
    # - Word Ladder -
    # 
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
    # 
    """
    ...
class _1047:
    """
    # - Remove All Adjacent Duplicates In String -
    # 
    """
    ...
class _173:
    """
    # - Binary Search Tree Iterator -
    # 
    """
    ...
class _1381:
    """
    # - Design a Stack With Increment Operation -
    # 
    """
    ...
class _356:
    """
    # - Line Reflection -
    # 
    """
    ...
class _1015:
    """
    # - Smallest Integer Divisible by K -
    # 
    """
    ...
class _155:
    """
    # - Min Stack -
    # 
    """
    ...
class _202:
    """
    # - Happy Number -
    # 
    """
    ...
class _862:
    """
    # - Shortest Subarray with Sum at Least K -
    # 
    """
    ...
class _503:
    """
    # - Next Greater Element II -
    # 
    """
    ...
class _218:
    """
    # - The Skyline Problem -
    # 
    """
    ...
class _678:
    """
    # - Valid Parenthesis String -
    # 
    """
    ...
class _349:
    """
    # - Intersection of Two Arrays -
    # 
    """
    ...
class _2008:
    """
    # - Maximum Earnings From Taxi -
    # 
    """
    ...
class _493:
    """
    # - Reverse Pairs -
    # 
    """
    ...
class _1344:
    """
    # - Angle Between Hands of a Clock -
    # 
    """
    ...
class _8:
    """
    # - String to Integer (atoi) -
    # 
    """
    ...
class _427:
    """
    # - Construct Quad Tree -
    # 
    """
    ...
class _489:
    """
    # - Robot Room Cleaner -
    # 
    """
    ...
class _843:
    """
    # - Guess the Word -
    # 
    """
    ...
class _1166:
    """
    # - Design File System -
    # 
    """
    ...
class _724:
    """
    # - Find Pivot Index -
    # 
    """
    ...
class _772:
    """
    # - Basic Calculator III -
    # 
    """
    ...
class _1539:
    """
    # - Kth Missing Positive Number -
    # 
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
    # 
    """
    ...
class _791:
    """
    # - Custom Sort String -
    # 
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
    # 
    """
    ...
class _1405:
    """
    # - Longest Happy String -
    # 
    """
    ...
class _419:
    """
    # - Battleships in a Board -
    # 
    """
    ...
class _85:
    """
    # - Maximal Rectangle -
    # 
    """
    ...
class _249:
    """
    # - Group Shifted Strings -
    # 
    """
    ...
class _616:
    """
    # - Add Bold Tag in String -
    # 
    """
    ...
class _416:
    """
    # - Partition Equal Subset Sum -
    # 
    """
    ...
class _96:
    """
    # - Unique Binary Search Trees -
    # 
    """
    ...
class _336:
    """
    # - Palindrome Pairs -
    # 
    """
    ...
class _179:
    """
    # - Largest Number -
    # 
    """
    ...
class _1029:
    """
    # - Two City Scheduling -
    # 
    """
    ...
class _1481:
    """
    # - Least Number of Unique Integers after K Removals -
    # 
    """
    ...
class _2104:
    """
    # - Sum of Subarray Ranges -
    # 
    """
    ...
class _166:
    """
    # - Fraction to Recurring Decimal -
    # 
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
    # 
    """
    ...
class _346:
    """
    # - Moving Average from Data Stream -
    # 
    """
    ...
class _1275:
    """
    # - Find Winner on a Tic Tac Toe Game -
    # 
    """
    ...
class _480:
    """
    # - Sliding Window Median -
    # 
    """
    ...
class _26:
    """
    # - Remove Duplicates from Sorted Array -
    # 
    """
    ...
class _241:
    """
    # - Different Ways to Add Parentheses -
    # 
    """
    ...
class _301:
    """
    # - Remove Invalid Parentheses -
    # 
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
    # 
    """
    ...
class _1366:
    """
    # - Rank Teams by Votes -
    # 
    """
    ...
class _279:
    """
    # - Perfect Squares -
    # 
    """
    ...
class _403:
    """
    # - Frog Jump -
    # 
    """
    ...
class _621:
    """
    # - Task Scheduler -
    # 
    """
    ...
class _741:
    """
    # - Cherry Pickup -
    # 
    """
    ...
class _19:
    """
    # - Remove Nth Node From End of List -
    # 
    """
    ...
class _99:
    """
    # - Recover Binary Search Tree -
    # 
    """
    ...
class _526:
    """
    # - Beautiful Arrangement -
    # 
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
    # 
    """
    ...
class _496:
    """
    # - Next Greater Element I -
    # 
    """
    ...
class _953:
    """
    # - Verifying an Alien Dictionary -
    # 
    """
    ...
