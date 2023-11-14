/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maxVolume = 0;
    let [left, right] = [0, height.length - 1];

    while (left < right) {
        const leftHeight = height[left];
        const rightHeight = height[right];
        const currVolume = (right - left) * Math.min(leftHeight, rightHeight);
        maxVolume = Math.max(maxVolume, currVolume);

        if (leftHeight < rightHeight){
            left++;
        } else {
            right--;
        }
    }
    return maxVolume
};