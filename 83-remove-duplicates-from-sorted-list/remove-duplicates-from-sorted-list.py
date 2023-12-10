# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            nextNode = curr.next
            while nextNode and nextNode.val == curr.val:
                curr.next = nextNode.next
                nextNode = nextNode.next

            curr = curr.next

        return head