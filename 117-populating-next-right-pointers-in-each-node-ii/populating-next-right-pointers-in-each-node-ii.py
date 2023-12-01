"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        queue = deque([root])
        res = []

        while len(queue) > 0:
            rowLength = len(queue)
            row = []

            for i in range(rowLength):
                curr = queue.popleft()
                row.append(curr)

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            for i, node in enumerate(row):
                if i + 1 < len(row):
                    node.next = row[i+1]

        return root