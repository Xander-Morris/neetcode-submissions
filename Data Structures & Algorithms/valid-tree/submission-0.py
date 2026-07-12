class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(i, parent):
            if i in visited:
                return False 
                
            visited.add(i)

            for connected in adj[i]:
                if connected == parent:
                    continue
                if not dfs(connected, i):
                    return False 
            
            return True 
        
        return dfs(0, -1) and len(visited) == n