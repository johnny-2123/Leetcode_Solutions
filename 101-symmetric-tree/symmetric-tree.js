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
var isSymmetric = function(root) {
    const isSameTree = (p, q) => {
        if (!p && !q) return true;
        if (!p || !q) return false;
        if (p.val !== q.val) return false;

        return isSameTree(p.left, q.right) && isSameTree(p.right, q.left)
    }

    return isSameTree(root, root)
};