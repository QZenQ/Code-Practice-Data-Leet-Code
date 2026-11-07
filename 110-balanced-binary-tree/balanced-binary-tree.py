# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    found = True
    def isBalanced(self, root: TreeNode | None) -> bool:

        
        def depthDiff(node):
            if not node:
                return 0

            h1 = depthDiff(node.left)
            h2 = depthDiff(node.right)

            if(abs(h1 - h2)>1):
                Solution.found = False
                print(abs(h1 - h2))
             
            return max(h1, h2) + 1

        if not root:
            return True    
        Solution.found = True
        depthDiff(root)

        return Solution.found
