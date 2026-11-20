# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def _traverse(node):
            if not node:
                return False

            if not node.left and not node.right:
                return node.val == target 
            
            for child in [node.left, node.right]:
                if not child:
                    continue
                
                if _traverse(child):
                    if child == node.left:
                        node.left = None
                    else:
                        node.right = None 

            return not node.left and not node.right and node.val == target

        if _traverse(root):
            root = None 

        return root 