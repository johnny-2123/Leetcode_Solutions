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

function partition(head: ListNode | null, x: number): ListNode | null {
    if (!head) return null;

    const leftNodes: ListNode[] = [];
    const rightNodes: ListNode[] = [];

    let curr = head;
    while (curr) {
        if (curr.val < x) {
            leftNodes.push(curr);    
        } else {
            rightNodes.push(curr);
        }
        const nextNode = curr.next;
        curr.next = null;
        curr = nextNode;
    }

    
    let leftHead: ListNode = new ListNode(null); 
    let leftTail: ListNode = leftHead
    for (const node of leftNodes) {
        leftTail.next = node;
        leftTail = node;
    }

    let rightHead: ListNode = new ListNode(null);
    let rightTail: ListNode = rightHead;
    for (const node of rightNodes) {
        rightTail.next = node;
        rightTail = node;
    }

    if (!leftHead.next) {
        leftHead.next = rightHead.next
    } else {
        leftTail.next = rightHead.next;
    }

    return leftHead.next
};