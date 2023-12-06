# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        
        res = []
        queue = deque([root])

        while len(queue) > 0:
            rowLength = len(queue)
            rowSum = 0

            for i in range(rowLength):
                curr = queue.popleft()
                rowSum += curr.val

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            rowAverage = rowSum / rowLength
            res.append(rowAverage)
        
        return res