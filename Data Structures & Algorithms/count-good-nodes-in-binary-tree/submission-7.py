# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        
        def _traverse(node, max_val):
            nonlocal res

            if not node:
                return
            
            if node.val >= max_val:
                res += 1
                max_val = node.val 
            
            for child in [node.left, node.right]:
                if not child:
                    continue
                _traverse(child, max_val)

        _traverse(root, root.val)

        return res