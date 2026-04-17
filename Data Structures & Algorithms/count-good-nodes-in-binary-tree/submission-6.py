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
            # I don't need to process each node within a level, but I could do that.
            node, val = q.popleft()

            # If the value of this node is >= the highest value we have seen so far
            # with respect to the node, then increase the result.
            if node.val >= val:
                res += 1
            
            for child in [node.left, node.right]:
                if not child:
                    continue
                
                # The new value we append for this child is the maximum of
                # the currently processed node's value, and the value it had stored.
                q.append((child, max(node.val, val)))

        return res