# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []

        def _dfs(node, numStr = ""):
            if not node: return
            numStr += f"{node.val}"
            
            if not node.left and not node.right:
                numbers.append(numStr)

            _dfs(node.left, numStr)
            _dfs(node.right, numStr)

        _dfs(root)
        
        res = 0

        for num in numbers:
            res += int(num)

        return res