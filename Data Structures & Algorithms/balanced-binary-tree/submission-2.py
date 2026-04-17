# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # [balanced, height] = what we return from here
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # both are balanced, and abs of height is <= 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # height is 1 + max of left and right height
            # we add 1 since we need to account for this node as well to return
            # to the parent
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]