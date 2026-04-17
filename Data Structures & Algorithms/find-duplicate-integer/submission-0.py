class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            # Where the number should be in the array.
            # For example, 2 should be in position 1. 5 should be in position 4.
            index = abs(num) - 1 

            if nums[index] < 0:
                return abs(num)

            nums[index] *= -1

        return -1