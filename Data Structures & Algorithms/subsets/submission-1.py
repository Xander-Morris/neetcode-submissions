class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, sub):
            if i == len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            backtrack(i + 1, sub)
            sub.pop()
            backtrack(i + 1, sub)
        
        backtrack(0, [])

        return res