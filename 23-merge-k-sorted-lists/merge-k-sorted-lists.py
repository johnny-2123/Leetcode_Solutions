# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newArr = []

        for subList in lists:
            cur = subList
            while cur:
                newArr.append([cur.val, cur])
                cur = cur.next
        newArr.sort(key = lambda x: x[0])
        print(newArr)
        dummy = ListNode()
        cur = dummy
        for val, node in newArr:
            cur.next = node
            cur = cur.next
        return dummy.next