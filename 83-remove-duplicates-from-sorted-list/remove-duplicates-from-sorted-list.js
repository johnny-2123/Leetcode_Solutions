/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let curr = head;
    while (curr) {
        let nextNode = curr.next;
        while (nextNode && nextNode.val === curr.val) {
            curr.next = nextNode.next;
            nextNode = nextNode.next;
        }
        curr = curr.next;
    }
    return head;
};