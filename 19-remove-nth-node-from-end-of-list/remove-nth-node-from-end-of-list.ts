/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    const dummy: ListNode = new ListNode(0, head);

    let count: number = 0;  
    let curr: ListNode = head;
    while (curr) {
        curr = curr.next;
        count++;
    }

    const target: number = count - n;

    count = 0;
    curr = dummy
    while (curr && count < target) {
        curr = curr.next;
        count++;
    }

    if (curr.next) {
        curr.next = curr.next.next;
    } else {
        curr.next = null;
    }
    return dummy.next
};