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
        
        mp = {} # [original] = new

        def _traverse(node):
            if node in mp:
                return mp[node]
            
            new_node = Node(node.val)
            mp[node] = new_node

            for neighbor in node.neighbors:
                if neighbor not in mp:
                    mp[neighbor] = _traverse(neighbor)
                
                new_node.neighbors.append(mp[neighbor])
            
            return new_node
        
        return _traverse(node)