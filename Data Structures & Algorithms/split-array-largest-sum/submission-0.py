from functools import cache 

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        @cache 
        def _traverse(i, k):
            if i == len(nums):
                return 0 if k == 0 else float('inf')
            if k == 0:
                return float('inf')

            res = float('inf')
            curr = 0

            for j in range(i, (len(nums) - k) + 1):
                curr += nums[j]
                res = min(res, max(curr, _traverse(j + 1, k - 1)))

            return res 

        return _traverse(0, k)