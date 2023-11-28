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
 * @return {boolean}
 */
var isBalanced = function(root) {

    let isBalanced = true;

    const _dfs = (node) => {
        if (!node) return 0;

        const leftHeight = _dfs(node.left);
        const rightHeight = _dfs(node.right);

        if (Math.abs(leftHeight - rightHeight) >= 2) {
            isBalanced = false;
        };

        return 1 + Math.max(leftHeight, rightHeight)
    }

    _dfs(root)
    return isBalanced;
};