class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build adjacency list to easily index down below 
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # build set of visited nodes 
        visited = set()

        def dfs(i, parent):
            # if we already visited this node, then we have a graph cycle, so it cannot be a valid tree
            if i in visited:
                return False 

            # add to set of visited nodes
            visited.add(i)

            for connected in adj[i]:
                # this would automatically make a false cycle detected, so don't do dfs on the parent
                if connected == parent:
                    continue
                # do dfs on this connected node while passing this current node as the parent 
                if not dfs(connected, i):
                    return False 
            
            # is a valid tree in this dfs call 
            return True 
        
        # dfs(0, -1) since we want node 0 to not be considered to actually have a parent node
        # in addition, we must visit all nodes, so len(visited) == n 
        return dfs(0, -1) and len(visited) == n