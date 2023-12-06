# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        orderedTreeValues = inOrderTraversal(root)
        minDiff = float("inf")

        for i in range(len(orderedTreeValues) - 1):
            diff = abs(orderedTreeValues[i] - orderedTreeValues[i+1])
            minDiff = min(minDiff, diff)
            
        return minDiff

def inOrderTraversal (node):
    if not node: return []

    left = inOrderTraversal(node.left)
    right = inOrderTraversal(node.right)

    return left + [node.val] + right
