/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let targetIdx = -1;
    let start = 0;
    let end = nums.length - 1;

    while (start <= end) {
        const mid = Math.floor((start + end) / 2);
        if (nums[mid] === target) {
            targetIdx = mid;
            break;
        } else if (target < nums[mid]) {
            end = mid - 1
        } else {
            start = mid + 1;
        } 
    }

    if (targetIdx === -1) return [-1, -1];

    start = targetIdx;
    let first = start
    while (start >= 0 && nums[start] === target) {
        start--;
    }
    end = targetIdx;
    while (end <= nums.length - 1 && nums[end] === target) {
        end++;
    }

    return [start + 1, end - 1];
};