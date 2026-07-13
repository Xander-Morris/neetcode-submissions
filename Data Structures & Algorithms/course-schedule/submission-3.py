class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            # a is the node that has its indegree incremented because the problem states that
            # you MUST take course b first if you want to take course a
            # meaning that a has a new dependency, that being b
            # indegree = number of dependencies before it = number of edges coming into it
            in_degree[a] += 1
            adj[b].append(a)
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited = 0

        while q:
            visited += 1
            node = q.popleft()
            
            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return visited == numCourses