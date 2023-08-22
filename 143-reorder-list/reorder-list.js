/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if (!head || !head.next) return head;

    let slow = head;
    let fast = head;

    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let list1 = head;
    let list2 = slow.next;
    slow.next = null;

    let curr = list2;
    let next = null;
    let prev = null;

    while (curr) {
        next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    list2 = prev;

    let curr1 = list1;
    console.log("curr1", curr1)
    let curr2 = list2;
    console.log("curr2", curr2)

    let newHead = new ListNode(); 
    let dummy = newHead; 

    while (curr1 && curr2) {
        dummy.next = curr1;
        curr1 = curr1.next;
        dummy = dummy.next;

        dummy.next = curr2;
        curr2 = curr2.next;
        dummy = dummy.next;
    }

    if(curr1) {
        dummy.next = curr1;
        curr1 = curr1.next
    }

    if (curr2) {
    dummy.next = curr2;
    }

    return newHead.next;
 


};