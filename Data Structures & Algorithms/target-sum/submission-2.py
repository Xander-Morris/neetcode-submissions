from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache 
        def _traverse(i, s):
            if i == len(nums):
                return s == target 
            
            return _traverse(i + 1, s + nums[i]) + _traverse(i + 1, s + -nums[i])
        
        return _traverse(0, 0)