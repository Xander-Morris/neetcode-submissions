class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Pick array ensures that each number is used only once per permutation.
        def backtrack(perm, pick):
            # The length of each permutation must be equal to the length of
            # the "nums" array.
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                # Skip numbers that have been picked in this permutation.
                if pick[i]:
                    continue

                perm.append(nums[i])
                pick[i] = True
                backtrack(perm, pick)
                perm.pop()
                pick[i] = False

        backtrack([], [False] * len(nums))

        return res