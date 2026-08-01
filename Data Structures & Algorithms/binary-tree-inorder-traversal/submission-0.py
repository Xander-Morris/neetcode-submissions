# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _traverse(node):
            if not node:
                return 
                
            nonlocal res

            _traverse(node.left)
            res.append(node.val)
            _traverse(node.right)

        _traverse(root)

        return res