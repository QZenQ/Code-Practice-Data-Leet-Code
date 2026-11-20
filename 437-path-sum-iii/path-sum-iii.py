# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        psums = defaultdict(int)
        psums[0] = 1
        count = 0

        def GetPaths(root, total):
            if not root:
                return 0

            count = 0

            total = total + root.val
            
            count = psums[total - targetSum]

            psums[total] = psums[total] + 1

            # print(f"for {root.val} count is  {count} and dict is {psums} and dist tp target os {targetSum - total} and total is {total}")

            # print("")
            count += GetPaths(root.left, total)
            count += GetPaths(root.right, total)

            psums[total] -= 1
            return count

        return GetPaths(root, 0)


        