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
var maxPathSum = function(root) {
    let res = -Infinity;

    const dfs = (node) => {
        if (!node) return 0;

        const left = dfs(node.left);
        const right = dfs(node.right);

        const totalSum = left + right + node.val;
        const leftSum = left + node.val;
        const rightSum = right + node.val;
       
        res = Math.max(res, node.val, leftSum, rightSum, totalSum);
        return Math.max(node.val, node.val + Math.max(left, right));
    }

    dfs(root);
    return res
};