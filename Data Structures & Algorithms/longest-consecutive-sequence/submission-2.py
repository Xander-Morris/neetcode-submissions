class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 in nums_set:
                continue
            
            k = num

            while k + 1 in nums_set:
                k += 1
            
            result = max(result, k - num + 1)

        return result