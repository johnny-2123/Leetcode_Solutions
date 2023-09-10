# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        cur = l1
        while cur:
            num1 = str(cur.val) + num1
            cur = cur.next

        num2 = ""
        cur = l2
        while cur:
            num2 = str(cur.val) + num2
            cur = cur.next

        total = int(num1) + int(num2)
        arr = list(reversed(str(total)))
        
        head = ListNode(int(arr[0]))
        cur = head
        for i in range(1, len(arr)):
            nextNode = ListNode(int(arr[i]))
            cur.next = nextNode
            cur = cur.next

        return head
        