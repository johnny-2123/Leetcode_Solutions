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
 * @return {number}
 */
var maxDepth = function(root) {
    let queue = [root];
    let count = 0;

    while(queue[0]) {
        let qLength = queue.length;
        let row = [];

        for (let i = 0; i < qLength; i++) {
            const currNode = queue.shift();
            row.push(currNode);

            if(currNode.left) queue.push(currNode.left)
            if(currNode.right) queue.push(currNode.right)
        }

        if(row) {
            count++;
        }
    }

    console.log("count", count)
    return count
    
};