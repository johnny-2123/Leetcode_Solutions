/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let left = 0;
    let right = 0;
    let steps = 0;
    while (right < nums.length - 1) {
        let maxIdx = right;
        for (let i = 0; i < right + 1; i++) {
            maxIdx = Math.max(maxIdx, i + nums[i]);
        };
        left = right + 1;
        right = maxIdx;
        steps++;
    }
    return steps
};