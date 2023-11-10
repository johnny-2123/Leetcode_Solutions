/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let [left, right] = [0, nums.length - 1];

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        const midNum = nums[mid]
        const leftNum = nums[left];
        const rightNum = nums[right];

        if (leftNum <= rightNum) {
            return leftNum;
        } else if (leftNum <= midNum) {
            left = mid + 1;
        } else {
            right = mid
        }
    }

    return nums[left]
};