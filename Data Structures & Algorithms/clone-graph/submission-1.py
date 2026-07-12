"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        mp = {} # old node to new node
        
        def dfs(old):
            if old in mp:
                return mp[old]
            
            mp[old] = Node(old.val)
            
            for nei in old.neighbors:
                new_nei_node = dfs(nei)
                mp[old].neighbors.append(new_nei_node)

            return mp[old]

        return dfs(node)