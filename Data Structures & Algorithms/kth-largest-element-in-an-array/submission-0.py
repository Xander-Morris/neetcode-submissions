class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for num in nums:
            heapq.heappush(pq, -num)

        for _ in range(k - 1):
            heapq.heappop(pq)

        return -heapq.heappop(pq)