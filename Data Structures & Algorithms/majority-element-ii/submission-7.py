class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0

        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            if (j - i) > (n // 3):
                res.append(nums[i])
            i = j

        return res