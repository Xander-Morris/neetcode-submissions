class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, sub, total):
            if total == target:
                res.append(sub[:])
                return
            elif i >= len(nums) or total > target:
                return
            
            sub.append(nums[i])
            backtrack(i, sub, total + nums[i])
            sub.pop()
            backtrack(i + 1, sub, total)
        
        backtrack(0, [], 0)

        return res