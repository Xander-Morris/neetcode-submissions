class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, sub, total):
            if total == target:
                res.append(sub[:])
                return
            elif total > target or i >= len(nums):
                return
            
            for n in range(i, len(nums)):
                if nums[n] > target:
                    continue
                
                sub.append(nums[n])
                backtrack(n, sub, total + nums[n])
                sub.pop()

        backtrack(0, [], 0)

        return res