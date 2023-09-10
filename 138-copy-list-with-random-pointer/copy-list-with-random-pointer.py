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
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            
            copyNext = oldToCopy.get(cur.next, None)
            copy.next = copyNext

            copyRandom = oldToCopy.get(cur.random, None)
            copy.random = copyRandom

            cur = cur.next

        return oldToCopy.get(head, None)
