# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            lst = []

            for _ in range(length):
                node = q.popleft()
                lst.append(node.val)

                for child in [node.left, node.right]:
                    if not child:
                        continue
                    
                    q.append(child)

            res.append(lst)
        
        return res