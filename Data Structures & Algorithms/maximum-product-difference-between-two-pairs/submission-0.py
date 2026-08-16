class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxh = []
        minh = []

        for num in nums:
            heapq.heappush(maxh, -num)
            heapq.heappush(minh, num)

        first, second = -heapq.heappop(maxh), -heapq.heappop(maxh)
        third, fourth = heapq.heappop(minh), heapq.heappop(minh)

        return (first * second) - (third * fourth)