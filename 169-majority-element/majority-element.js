/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    nums.sort((a, b) => a - b)
    const n = nums.length / 2;
    let count = 0;
    let currNum = nums[0]

    for (const num of nums){
        if (num !== currNum) {
            count = 1
            currNum = num
        } else {
            count++;
        }

        if (count > n) return currNum
    }
};