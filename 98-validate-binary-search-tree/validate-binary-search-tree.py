# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        Q = [(root, float('-inf'), float('inf'))]

        while Q:
            cn, low, high = Q.pop(0)

            if cn.val >= high or cn.val <= low:
                return False

            if cn.left:
                Q.append((cn.left, low ,cn.val))

            
            if cn.right:
                Q.append((cn.right, cn.val, high))
        
        return True
        