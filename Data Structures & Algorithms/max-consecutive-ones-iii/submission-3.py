class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = l = 0
        count = {}

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1

            while count.get(0, 0) > k:
                count[nums[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res