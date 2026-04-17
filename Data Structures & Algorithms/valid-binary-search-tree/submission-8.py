# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # node, left, right
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()

            if not (left < node.val < right):
                return False
                
            # The "right" value for node.left is node.val because
            # the current node is to the right of node.left, intuitively. 
            # Just think about the graph in a visual sense.
            if node.left:
                q.append((node.left, left, node.val))

            # The "left" value for node.right is node.val because
            # the current node is to the left of node.right, intuitively. 
            # Just think about the graph in a visual sense.
            if node.right:
                q.append((node.right, node.val, right))

        return True