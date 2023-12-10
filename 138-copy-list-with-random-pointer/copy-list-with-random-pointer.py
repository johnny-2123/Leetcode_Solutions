"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy.get(curr)
            copyNext = oldToCopy.get(curr.next, None)
            copy.next = copyNext

            copyRandom = oldToCopy.get(curr.random, None)
            copy.random = copyRandom
            curr = curr.next

        return oldToCopy.get(head, None)