# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(p.val == q.val): return p.val

        parents = {root:None}
        
        pre = root
        Q = [root]

        while(Q):
            pre = Q.pop(0)

            if pre.left:
                parents[pre.left] = pre
                Q.append(pre.left)

            if pre.right:
                parents[pre.right] = pre
                Q.append(pre.right)


        pre = p
        data = set()

        while(pre):
            data.add(pre)
            pre = parents[pre]

        
        pre = q

        while(pre):
            if(pre in data):
                return pre
            pre = parents[pre]

         