class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 in nums_set:
                continue
            
            length = 1
            k = num

            while k + 1 in nums_set:
                length += 1 
                k += 1
            
            result = max(result, length)

        return result