class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_counts = {0: 1}     
        curr = res = 0

        for num in nums:
            curr += num

            if curr - k in sum_counts:
                res += sum_counts[curr - k]

            sum_counts[curr] = sum_counts.get(curr, 0) + 1

        return res  