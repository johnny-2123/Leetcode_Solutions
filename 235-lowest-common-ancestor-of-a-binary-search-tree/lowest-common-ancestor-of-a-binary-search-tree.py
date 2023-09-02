# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val = root.val
        pVal = p.val
        qVal = q.val
        if val > pVal and val > qVal:
            return self.lowestCommonAncestor(root.left, p, q)
        if val < pVal and val < qVal:
            return self.lowestCommonAncestor(root.right, p, q)
        if val == pVal or val == qVal:
            return root
        if val > pVal and val < qVal:
            return root
        if val < pVal and val > qVal:
            return root
        