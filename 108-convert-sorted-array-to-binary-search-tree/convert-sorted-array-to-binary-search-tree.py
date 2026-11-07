# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        Q = []
        mid = (len(nums) - 1)//2
        root = TreeNode(nums[mid])
        Q.append((root, 0, len(nums) - 1))

        while Q:
            node, left, right = Q.pop()
            mid = (left + right)//2

            if(left <= mid - 1):
                lmid = (left + mid - 1)//2
                lnode = TreeNode(nums[lmid])
                node.left = lnode
                Q.append((lnode, left, mid - 1))

            if(right >= mid + 1):
                rmid = (right + mid + 1)//2
                rnode = TreeNode(nums[rmid])
                node.right = rnode
                Q.append((rnode,mid + 1, right))


        return root
            

        