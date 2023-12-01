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

        while len(queue) > 0:
            rowLength = len(queue)

            for i in range(rowLength):
                curr = queue.popleft()
                if i < rowLength - 1:
                    curr.next = queue[0]

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

        return root