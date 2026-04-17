class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            m = (l + r) // 2
            result = min(result, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return result