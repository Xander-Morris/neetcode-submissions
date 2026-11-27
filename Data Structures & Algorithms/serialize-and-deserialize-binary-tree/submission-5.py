# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        vals = []

        def _preorder(node):
            if not node:
                vals.append("None")
                return
            vals.append(str(node.val))
            _preorder(node.left)
            _preorder(node.right)
            
        _preorder(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        vals = deque(data.split(","))
        
        def _build():
            val = vals.popleft()

            if val == "None":
                return None

            node = TreeNode(int(val))
            node.left = _build()
            node.right = _build()
            
            return node

        return _build()