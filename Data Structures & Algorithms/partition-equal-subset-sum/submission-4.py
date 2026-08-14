class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # odd sum cant be split equally into two without remainder
        if total % 2 != 0:
            return False 
        
        half_target = total // 2
        n = len(nums)
        memo = [[-1] * (total + 1) for _ in range(n + 1)]

        def _traverse(so_far, i, nums_taken):
            if memo[i][so_far] != -1:
                return memo[i][so_far]
            if so_far == half_target:
                return True
            if so_far > half_target or i >= len(nums):
                return False
            
            memo[i][so_far] = (_traverse(so_far + nums[i], i + 1, nums_taken + 1) or _traverse(so_far, i + 1, nums_taken))

            return memo[i][so_far]

        return _traverse(0, 0, 0)