class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, pick):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            elif len(perm) > len(nums):
                return
            
            for n in range(len(nums)):
                if pick[n]:
                    continue
                
                pick[n] = True
                perm.append(nums[n])
                backtrack(perm, pick)
                pick[n] = False
                perm.pop()
        
        backtrack([], [False] * len(nums))

        return res