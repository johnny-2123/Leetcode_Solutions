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
var getMinimumDifference = function(root) {
    const inOrderValues = _dfs(root);
    let min = Infinity;

    for (let i = 0; i < inOrderValues.length - 1; i++) {
        const diff = Math.abs(inOrderValues[i] - inOrderValues[i+1]);
        min = Math.min(min, diff);
    }

    return min;
};

const _dfs = (node) => {
    if (!node) return [];

    const left = _dfs(node.left);
    const right = _dfs(node.right);

    return left.concat([node.val]).concat(right)
}