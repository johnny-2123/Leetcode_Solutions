/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    if (nums.length <= 1) {
        return 0
    }
    let left = 0;
    let right = 0;
    let res = 0;
    while (right < nums.length - 1) {
        // keep track how far you can get from this window
        let maxIdx = 0;
        for (let i = 0; i <= right; i++) {
            maxIdx = Math.max(maxIdx, i + nums[i]);
        };
        left = right + 1;
        right = maxIdx;
        res++;
    }
    return res
};