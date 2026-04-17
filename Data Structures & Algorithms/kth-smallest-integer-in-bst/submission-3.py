# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []

        def addToPQ(root):
            nonlocal pq

            if not root:
                return

            heapq.heappush(pq, root.val)

            addToPQ(root.left)
            addToPQ(root.right)

        addToPQ(root)

        for _ in range(k - 1):
            heapq.heappop(pq)

        return heapq.heappop(pq)  