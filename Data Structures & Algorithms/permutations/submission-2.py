class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, pick):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                if pick[i]:
                    continue

                perm.append(nums[i])
                pick[i] = True
                backtrack(perm, pick)
                perm.pop()
                pick[i] = False

        backtrack([], [False] * len(nums))

        return res