class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def _traverse(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(_traverse(i + 1), nums[i] + _traverse(i + 2))

            return memo[i]

        return _traverse(0)