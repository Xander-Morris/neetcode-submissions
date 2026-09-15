from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_to_courses = defaultdict(set)
        adj = defaultdict(list)

        for pre, nxt in prerequisites:
            adj[pre].append(nxt)
        
        for pre, nxt in prerequisites:
            q = deque([nxt])
            visited = set([nxt])

            while q:
                node = q.popleft()
                pre_to_courses[pre].add(node)

                for a in adj[node]:
                    if a in visited:
                        continue

                    visited.add(a)
                    q.append(a)
        
        return [node in pre_to_courses[pre] for pre, node in queries]