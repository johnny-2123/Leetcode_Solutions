# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        count = 1
        curr = head
        while curr:
            curr = curr.next
            count += 1
       
        target = count - n

        count = 1
        curr = dummy
        while curr and count < target:
            curr = curr.next
            count += 1
       
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = null
       
        return dummy.next
