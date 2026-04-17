class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        pq = []

        for num in count:
            heapq.heappush(pq, (-count[num], num))

        for _ in range(k):
            top = heapq.heappop(pq)
            res.append(top[1])

        return res