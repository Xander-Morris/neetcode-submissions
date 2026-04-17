class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix_prod = defaultdict(list)
        suffix_prod = defaultdict(list)
        i = 0
        
        while i < len(nums):
            prev_i = i - 1
            new_prod = prefix_prod[prev_i] * nums[prev_i] if prev_i >= 0 else 1
            prefix_prod[i] = new_prod
            i += 1

        i = len(nums)

        while i >= 0:
            prev_i = i + 1
            new_prod = suffix_prod[prev_i] * nums[prev_i] if prev_i < len(nums) else 1
            suffix_prod[i] = new_prod
            i -= 1

        i = 0

        while i < len(nums):
            result.insert(len(result), prefix_prod[i] * suffix_prod[i])
            i += 1
        
        return result
