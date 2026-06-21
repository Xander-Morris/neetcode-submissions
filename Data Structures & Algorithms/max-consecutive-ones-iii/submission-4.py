class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = l = 0
        count = {}

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1

            # while i have more 0's than i can convert to 1's, continue to push l pointer up
            while count.get(0, 0) > k:
                count[nums[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res