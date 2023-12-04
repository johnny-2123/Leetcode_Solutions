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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    if (!root) return false;

    const _dfs = (node, sum = 0) => {
        if (!node) return false;  
        sum += node.val;

        if (!node.left && !node.right) {
            if (sum === targetSum){
                return true;
            } else {
                return false;
            }
        }
        return _dfs(node.left, sum) || _dfs(node.right, sum);
    }
    return _dfs(root)
};