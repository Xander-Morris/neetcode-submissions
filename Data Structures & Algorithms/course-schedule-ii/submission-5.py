class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            in_degree[a] += 1
            adj[b].append(a)
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            node = q.popleft()
            res.append(node)

            for nxt in adj[node]:
                in_degree[nxt] -= 1
                if in_degree[nxt] > 0:
                    continue
                q.append(nxt)

        return res if len(res) == numCourses else []