# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        Q =[]
        Q.append(root)
        result = []
        
        while Q:
            level = []

            for _ in range(len(Q)):                
                node = Q.pop(0)

                
                if(node.left != None):
                    Q.append(node.left)
               

                if(node.right !=None):
                    Q.append(node.right)

                
                level.append(node.val)

            result.append(level)
                        
         
        return result