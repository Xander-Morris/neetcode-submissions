class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            in_degree[a] += 1
            adj[b].append(a)
        
        q = deque([course for course in range(numCourses) if in_degree[course] == 0])
        visited = 0

        while q:
            node = q.popleft()
            visited += 1

            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return visited == numCourses