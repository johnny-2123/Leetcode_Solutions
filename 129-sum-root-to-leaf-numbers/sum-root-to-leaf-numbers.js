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
var sumNumbers = function(root) {
    const numbers = [];

    const _dfs = (node, numStr = "") => {
        if (!node) return;
        numStr += node.val.toString();

        if (!node.left && !node.right){
            numbers.push(parseInt(numStr))
        }

        _dfs(node.left, numStr);
        _dfs(node.right, numStr);
    }

    _dfs(root);

    let res = 0;
    for (const num of numbers) {
        res += num;
    }

    return res;
};