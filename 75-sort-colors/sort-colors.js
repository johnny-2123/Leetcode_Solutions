/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */


var sortColors = function(nums) {
    for(let i = 1; i < nums.length; i++){
        for(let j = i; j > 0; j--) {
            const currNum = nums[j];
            const prevNum = nums[j - 1];
            if(currNum < prevNum) {
                [nums[j], nums[j - 1]] = [nums[j -1 ], nums[j]]
            } else {
                break
            }
        }
    }
};