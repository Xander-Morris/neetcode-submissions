class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        pq = []

        for num in set(nums):
            heapq.heappush(pq, (-count[num], num))

        i = 0
        
        while pq and i < k:
            pri, num = heapq.heappop(pq)
            result.insert(len(result), num)
            i += 1

        return result