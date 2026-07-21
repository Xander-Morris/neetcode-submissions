# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def _search(node):
            if not node:
                return

            nonlocal res
            if low <= node.val <= high:
                res += node.val
            _search(node.left)
            _search(node.right)

        _search(root)

        return res