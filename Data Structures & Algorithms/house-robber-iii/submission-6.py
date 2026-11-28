# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # flag = robbed parent of current node
        @cache
        def _traverse(node, flag):  
            if not node:
                return 0

            # skipping robbing this node 
            res = _traverse(node.left, False) + _traverse(node.right, False)
            
            if not flag:
                # simulate 
                res = max(res, node.val + _traverse(node.left, True) + _traverse(node.right, True))

            return res

        return _traverse(root, False)