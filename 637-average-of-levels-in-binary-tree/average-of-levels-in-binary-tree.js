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
var averageOfLevels = function(root) {
    if (!root) return [];

    const res = [];
    const queue = [root];

    while (queue.length > 0) {
        const rowLength = queue.length;
        let rowSum = 0;

        for (let i = 0; i < rowLength; i++) {
            const curr = queue.shift();
            rowSum += curr.val;

            if(curr.left) queue.push(curr.left);
            if(curr.right) queue.push(curr.right);
        }   
        const rowAverage = rowSum / rowLength;
        res.push(rowAverage);
    }
    return res;
};