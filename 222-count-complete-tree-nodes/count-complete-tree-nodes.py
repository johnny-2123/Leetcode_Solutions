# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append(root)

        count =  0
        while len(queue) > 0:
            qLength = len(queue)
            for i in range(qLength):
                node = queue.pop(0)
                if node: count += 1
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
        return count 