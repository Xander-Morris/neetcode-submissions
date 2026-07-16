class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {node: [] for node in range(1, n + 1)}
        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[k] = 0

        for source, target, time in times:
            adj[source].append((target, time))

        pq = [(0, k)]
        total = 0

        while pq:
            dist, node = heapq.heappop(pq)

            for target, time in adj[node]:
                new_time = time + dist 
                if distances[target] > new_time:
                    distances[target] = new_time
                    heapq.heappush(pq, (new_time, target))

        max_dist = max(distances.values())

        return max_dist if max_dist != float('inf') else -1