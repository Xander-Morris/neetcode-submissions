class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            The length of a subset can range from 0 elements to the length of the
            "nums" array.
        """
        res = []
        nums.sort()

        def backtrack(i, sub):
            if i == len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            backtrack(i + 1, sub)
            sub.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, sub)

        backtrack(0, [])

        return res