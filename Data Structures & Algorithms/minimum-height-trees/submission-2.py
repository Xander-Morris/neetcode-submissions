from collections import deque 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        heights = {i: float('inf') for i in range(n)}
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        for i in range(n):
            level = 0
            visited = set([i])  
            q = deque([i])

            while q:
                for _ in range(len(q)):
                    top = q.popleft()

                    for nxt in adj[top]:
                        if nxt in visited:
                            continue
                        
                        visited.add(nxt)
                        q.append(nxt)

                level += 1
            
            heights[i] = level 

        smallest_height = min(val for val in heights.values())

        return [i for i in range(n) if heights[i] == smallest_height]