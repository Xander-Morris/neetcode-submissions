# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = float('-inf')

        def _traverse(node):
            nonlocal ans

            if not node:
                return 0

            left_trav = max(0, _traverse(node.left))
            right_trav = max(0, _traverse(node.right))

            ans = max(ans, node.val + left_trav + right_trav)

            return node.val + max(left_trav, right_trav)

        _traverse(root)

        return ans