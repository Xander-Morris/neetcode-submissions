class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        #if n <= 1:
            #return True 

        i = 0
        while i < n - 1:
            max_i = max_step_after = 0
            for step_size in range(1, nums[i] + 1):
                next_i = i + step_size
                if next_i >= n:
                    break
                step_after = next_i + nums[next_i]
                if step_after >= max_step_after:
                    max_step_after = step_after
                    max_i = next_i
            if max_i <= i:
                return False 
            i = max_i

        return i >= n - 1