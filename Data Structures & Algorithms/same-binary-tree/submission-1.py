# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If one is null while the other is not null, then they are not the same.
        if (not p and q) or (p and not q): return False
        # If both are null, then they are the same.
        if not p and not q: return True
        # If their values are not equal, then they are not the same. 
        if p.val != q.val: return False

        # Compare the left and right subtrees of each tree, respectively. 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)