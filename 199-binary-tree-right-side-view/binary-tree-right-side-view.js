/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
    if (!root) return []
    const queue = [root]
    const res = []

    while (queue.length > 0) {
        const rowLength = queue.length;
        const row = []

        for (let i = 0; i < rowLength; i++) {
            const curr = queue.shift();
            row.push(curr.val)

            if (curr.left) queue.push(curr.left);
            if (curr.right) queue.push(curr.right);
        }

        res.push(row[row.length - 1])
    }
    return res;
};