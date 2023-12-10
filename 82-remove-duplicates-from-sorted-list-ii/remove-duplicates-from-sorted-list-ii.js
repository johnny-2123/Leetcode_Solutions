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
    const noDuplicates = [];

    let curr = head;
    let prev = null;
    while (curr) {
        let hasDuplicate = false;
        const nextNode = curr.next;
        
        if (prev && prev.val === curr.val) hasDuplicate = true;
        if (nextNode && nextNode.val === curr.val) hasDuplicate = true;
        
        if (!hasDuplicate) noDuplicates.push(curr)
        prev = curr;
        curr = curr.next
    }

    if (noDuplicates.length === 0) return null;

    for (let i = 0; i < noDuplicates.length - 1; i++) {
        const curr = noDuplicates[i];
        curr.next = noDuplicates[i + 1];
    }
    const lastNode = noDuplicates[noDuplicates.length - 1];
    lastNode.next = null;
    return noDuplicates[0]
};