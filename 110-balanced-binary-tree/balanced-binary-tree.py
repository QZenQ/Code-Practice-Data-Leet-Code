# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: TreeNode | None) -> bool:

        
        def depthDiff(node):
            if not node:
                return 0

            h1 = depthDiff(node.left)

            if(h1 == -1):return -1

            h2 = depthDiff(node.right)

            if h2 == -1: return -1

            if(abs(h1 - h2)>1):
                return -1
             
            return max(h1, h2) + 1

        if not root:
            return True    
        
        return depthDiff(root) != -1

        
