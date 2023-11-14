/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maxArea = -Infinity;
    let left = 0; 
    let right = height.length - 1;

    while (left < right) {
        const leftHeight = height[left];
        const rightHeight = height[right];

        const currArea = Math.min(leftHeight, rightHeight) * (right - left);

        maxArea = Math.max(currArea, maxArea);

        if(leftHeight < rightHeight) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea

};