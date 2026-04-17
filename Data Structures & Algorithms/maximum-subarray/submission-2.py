class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Stores the result (maximum sum found so far)
        res = nums[0]
        
        # Maximum sum of subarray ending at current position
        maxEnding = nums[0]

        for i in range(1, len(nums)):
            # Either extend the previous subarray or start 
            # new from current element
            maxEnding = max(maxEnding + nums[i], nums[i])
            
            # Update result if the new subarray sum is larger
            res = max(res, maxEnding)
        
        return res