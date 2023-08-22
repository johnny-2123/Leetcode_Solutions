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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    let queue = [];
    queue.push(root);
    
    let output = [];

    while(queue[0]) {
        const qLength = queue.length;
        let row = [];

        for (let i = 0; i < qLength; i++) {
            const curr = queue.shift();
            row.push(curr.val)
            if(curr.left) queue.push(curr.left);
            if(curr.right) queue.push(curr.right);

        }

        if(row) {
            output.push(row)
        }
    }
    return output;
};