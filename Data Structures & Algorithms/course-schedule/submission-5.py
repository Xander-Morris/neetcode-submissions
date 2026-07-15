class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            in_degree[a] += 1
            adj[b].append(a)
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited = 0

        while q:
            visited += 1
            node = q.popleft()

            for nxt in adj[node]:
                in_degree[nxt] -= 1
                if in_degree[nxt] > 0:
                    continue
                q.append(nxt)

        return visited == numCourses