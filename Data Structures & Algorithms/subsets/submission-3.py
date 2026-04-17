class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, sub):
            # If we have reached the index equal to the length of the nums array,
            # meaning we are out of bounds now,
            # then append the subset using the sub[:] syntax. 
            if i == len(nums):
                res.append(sub[:])
                return
            
            # Search solutions including this number at nums[i]
            sub.append(nums[i])
            backtrack(i + 1, sub)
            sub.pop() # Pop it off to backtrack
            backtrack(i + 1, sub) # Search solutions without this number
        
        backtrack(0, [])

        return res