# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = [True]

        def dfs(node):
            if not node: 
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if abs(leftHeight - rightHeight) >= 2: 
                isBalanced[0] = False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return isBalanced[0]
        