/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    const oldToCopy = new Map();

    let curr = head
    while (curr) {
        const copy = new Node(curr.val);
        oldToCopy.set(curr, copy);
        curr = curr.next
    }

    curr = head
    while (curr) {
        const copy = oldToCopy.get(curr);
        const copyNext = oldToCopy.get(curr.next) || null;
        copy.next = copyNext;

        const copyRandom = oldToCopy.get(curr.random) || null;
        copy.random = copyRandom;
        curr = curr.next;
    }
    return oldToCopy.get(head) || null;
};