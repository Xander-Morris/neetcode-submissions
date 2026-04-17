class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = defaultdict(int)
        suffix = defaultdict(int)
        curr_prod = 1

        for i in range(len(nums)):
            prefix[i] = curr_prod
            curr_prod *= nums[i]

        curr_prod = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = curr_prod
            curr_prod *= nums[i]

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result