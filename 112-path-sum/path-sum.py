# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        def _dfs(node, sum, target):
            if not node: return False
            sum += node.val

            if not node.left and not node.right:
                if sum == target:
                    return True
                else:
                    return False
            
            return _dfs(node.left, sum, target) or _dfs(node.right, sum, target)
        
        return _dfs(root, 0, targetSum)