class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        pq = []

        for point in points:
            dist = math.sqrt((0 - point[0]) ** 2  + (0 - point[1]) ** 2)
            heapq.heappush(pq, (dist, point))

        for _ in range(k):
            _, point = heapq.heappop(pq)
            res.append(point)

        return res