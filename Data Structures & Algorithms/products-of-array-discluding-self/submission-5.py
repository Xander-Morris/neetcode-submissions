class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix_prod = defaultdict(list)
        suffix_prod = defaultdict(list)
        curr_prod = 1

        for i in range(len(nums)):
            prefix_prod[i] = curr_prod 
            curr_prod *= nums[i]

        curr_prod = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix_prod[i] = curr_prod
            curr_prod *= nums[i]

        for i in range(len(nums)):
            result.append(prefix_prod[i] * suffix_prod[i])

        return result