class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # odd sum cant be split equally into two without remainder
        if total % 2 != 0:
            return False 
        
        half_target = total // 2

        def _traverse(so_far, i, nums_taken):
            if so_far == half_target:
                return True
            if so_far > half_target or i >= len(nums):
                return False
            
            return _traverse(so_far + nums[i], i + 1, nums_taken + 1) or _traverse(so_far, i + 1, nums_taken)

        return _traverse(0, 0, 0)