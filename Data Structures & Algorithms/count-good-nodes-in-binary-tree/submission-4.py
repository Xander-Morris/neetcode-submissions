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
        q.append((root,-float('inf')))

        while q:
            node, maxval = q.popleft()

            if node.val >= maxval:
                res += 1

            new_max_val = max(maxval, node.val)

            for child in [node.left, node.right]:
                if not child:
                    continue
                    
                q.append((child, new_max_val))

        return res