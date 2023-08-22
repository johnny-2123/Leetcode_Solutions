/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let [slow, fast] = [head, head];

    let count = 1;
    while(count <= n) {
        fast = fast.next;
        count++;
    }


    if (!fast) {
        return head.next;
    }

    while (fast.next){
        slow = slow.next;
        fast = fast.next;
    }

    console.log("slow", slow)
    console.log("fast", fast)

    slow.next = slow.next.next;

    return head;


    
};