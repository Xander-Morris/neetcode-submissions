class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        pq = []

        for num in count:
            heapq.heappush(pq, (-count[num], num))

        for _ in range(k):
            _, num = heapq.heappop(pq)
            res.append(num)

        return res