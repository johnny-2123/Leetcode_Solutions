# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def inOrderTraversal(self, root):
        if not root:
            return []

        left = self.inOrderTraversal(root.left)
        right = self.inOrderTraversal(root.right)

        return left + [root.val] + right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        orderedNodes = self.inOrderTraversal(root)
        print(orderedNodes)
        return  orderedNodes[k - 1]