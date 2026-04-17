# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        q.append((root, root.val - 1))

        while q:
            node, val = q.popleft()

            if node.val >= val:
                res += 1
            
            for child in [node.left, node.right]:
                if not child:
                    continue
                
                q.append((child, max(node.val, val)))

        return res