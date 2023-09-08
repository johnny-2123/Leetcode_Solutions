# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            totalSum = sum([node.val, left, right]) 
            leftSum = sum([node.val, left])
            rightSum = sum([node.val, right])
            maxSum = max(node.val, totalSum, leftSum, rightSum)
            if maxSum > res:
                res = maxSum

            return max(node.val + max(left, right), node.val)
    
        dfs(root)
        return res