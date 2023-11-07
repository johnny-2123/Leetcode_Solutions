/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    const breakpoint = k % nums.length;
    if (breakpoint === 0) return;
    const length = nums.length;

    const arr1 = nums.slice(-breakpoint);
    const arr2 = nums.slice(0, length - breakpoint);
    nums.splice(0, length, ...arr1, ...arr2);
};