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
var countNodes = function(root) {
    let queue = [root];
    let count = 0;

    while(queue[0]) {
        const currNode = queue.shift();
        count++;

        if(currNode.left) queue.push(currNode.left);
        if(currNode.right) queue.push(currNode.right);
    }

    console.log("count", count);
    return count;
    
};