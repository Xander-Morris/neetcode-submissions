class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, sub, total):
            if total == target:
                # Append the valid solution.
                res.append(sub[:])
                return
            elif i >= len(nums) or total > target:
                # It is invalid, so just stop.
                return
            
            sub.append(nums[i])
            backtrack(i, sub, total + nums[i]) # Search solutions with this number.
            sub.pop() # Pop it off to backtrack.
            backtrack(i + 1, sub, total) # Search solutions skipping this number.
        
        backtrack(0, [], 0)

        return res