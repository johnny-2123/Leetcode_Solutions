# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None

        leftNodes = []
        rightNodes = []

        curr = head
        while curr:
            if curr.val < x:
                leftNodes.append(curr)
            else:
                rightNodes.append(curr)
            nextNode = curr.next
            curr.next = None
            curr = nextNode
        
        leftHead = ListNode(None)
        leftTail = leftHead
        for node in leftNodes:
            leftTail.next = node
            leftTail = node
        
        rightHead = ListNode(None)
        rightTail = rightHead
        for node in rightNodes:
            rightTail.next = node
            rightTail = node
        
        if not leftHead.next:
            leftHead.next = rightHead.next
        else:
            leftTail.next = rightHead.next
        
        return leftHead.next