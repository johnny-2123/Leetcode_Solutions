# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        noDuplicates = []

        curr = head
        prev = None
        while curr:
            hasDuplicate = False
            nextNode = curr.next
            if prev and prev.val == curr.val:
                hasDuplicate = True
            if nextNode and nextNode.val == curr.val:
                hasDuplicate = True
            
            if not hasDuplicate:
                noDuplicates.append(curr)
            prev = curr
            curr = curr.next

        for i in range(len(noDuplicates) - 1):
            curr = noDuplicates[i]
            curr.next = noDuplicates[i + 1]

        if len(noDuplicates) == 0: return None

        lastNode = noDuplicates[-1]
        if lastNode:
            lastNode.next = None
        return noDuplicates[0]
