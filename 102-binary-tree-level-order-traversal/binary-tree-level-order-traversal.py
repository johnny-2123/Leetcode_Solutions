# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append(root)
        res = []

        while len(queue) > 0:
            rowLength = len(queue)
            row = []

            for i in range(rowLength):
                curr = queue.popleft()
                row.append(curr.val)

                if (curr.left): queue.append(curr.left)
                if (curr.right): queue.append(curr.right)

            res.append(row)
        return res
