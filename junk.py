from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        limit = 0
        for i in range(len(nums)):
            if i > limit:
                return False
            limit = max(limit, i + nums[i])
        return True

Solution().canJump([2,3,1,1,4])

# [2,3,1,1,4]
# [3,2,1,0,4]
