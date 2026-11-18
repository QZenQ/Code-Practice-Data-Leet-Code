# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
                 

        def sameTree(root: TreeNode, subRoot: TreeNode):
            Q = [(root, subRoot)]

            while(Q):
                rn, srn = Q.pop(0)

                if(not rn and not srn): continue
                if(not rn or not srn or rn.val != srn.val): return False

                Q.append((rn.left, srn.left))
                Q.append((rn.right, srn.right))

            return True
                 
        Q = [root]
        res = None        

        while(Q):
            res = Q.pop(0)

            if(res.val == subRoot.val): 
                if(sameTree(res, subRoot)):
                    return True

            if(res.left):
                Q.append(res.left)
            
            if(res.right):
                Q.append(res.right)

        return False


        

        