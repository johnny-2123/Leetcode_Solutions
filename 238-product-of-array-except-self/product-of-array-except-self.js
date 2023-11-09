/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const result = [];
    let preFix = 1;

    for (let i = 0; i < nums.length; i++) {
        result[i] = preFix;
        preFix *= nums[i];
    }

    let postFix = 1;

    for(let k = nums.length - 1; k >= 0; k--){
        result[k] *= postFix;
        postFix *= nums[k];
    }

    return result
};