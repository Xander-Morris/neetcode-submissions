class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        pq = []

        for num in count:
            """
                -count[num] to technically make it a "max-heap"
                since Python internally uses a min-heap for the heapq class
            """
            heapq.heappush(pq, (-count[num], num))

        for _ in range(k):
            count, num = heapq.heappop(pq)
            res.append(num)

        return res