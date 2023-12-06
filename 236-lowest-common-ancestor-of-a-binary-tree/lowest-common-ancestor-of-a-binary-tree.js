/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    
    const _dfs = (node) => {
        if (!node) return null;
        if(node.val === p.val || node.val === q.val) return node;

        const left = _dfs(node.left);
        const right = _dfs(node.right);

        if (left && right) {
            return node;
        } else if (left) {
            return left;
        } else {
            return right;
        }
    }
    return _dfs(root);
};