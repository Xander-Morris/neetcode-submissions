# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            # If both are greater than the current value,
            # then search in the right side.
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both are less than the current value,
            # then search in the left side.
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
            # Return the current node.
                return curr

        return None