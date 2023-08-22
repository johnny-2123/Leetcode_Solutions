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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSameTree = (p, q) => {
  if(!p && !q) return true;
  if(!p || !q) return false;
  if(p.val !== q.val) return false;

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

var isSubtree = function(root, subRoot) {
    let queue = [root];

    while(queue[0]) {
      const currNode = queue.shift();

      if(isSameTree(currNode, subRoot)) {
        return true;
      } else {
        if(currNode.left) (queue.push(currNode.left));
        if(currNode.right) (queue.push(currNode.right));
      }
    }

    return false
};