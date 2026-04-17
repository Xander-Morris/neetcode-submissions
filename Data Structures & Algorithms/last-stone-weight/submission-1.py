class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []

        for stone in stones:
            heapq.heappush(pq, -stone)
        
        while len(pq) > 1:
            top_1 = heapq.heappop(pq)
            top_2 = heapq.heappop(pq)

            if top_1 < top_2:
                heapq.heappush(pq, -(top_2 - top_1))
        
        return -heapq.heappop(pq) if pq else 0