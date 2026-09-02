class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []

        for n in arr:
            heapq.heappush(pq, (abs(n - x), n))

        res = []

        while len(res) < k:
            _, n = heapq.heappop(pq)
            res.append(n)
        
        res.sort()
        
        return res