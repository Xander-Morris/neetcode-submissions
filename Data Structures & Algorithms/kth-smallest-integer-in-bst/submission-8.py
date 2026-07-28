# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        def _traverse(node):
            nonlocal nums

            if not node:
                return
            
            _traverse(node.left)
            nums.append(node.val)
            _traverse(node.right)

        _traverse(root)

        return nums[k - 1]