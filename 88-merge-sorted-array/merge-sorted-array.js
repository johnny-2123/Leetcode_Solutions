/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
let i = m + n - 1;
m--;
n--;

while (i >= 0) {
    const num1 = nums1[m];
    const num2=  nums2[n];

    if (m >= 0 && n >= 0) {
        if (num1 >= num2) {
            nums1[i] = num1;
            m--;
        } else {
            nums1[i] = num2;
            n--;
        }
    } else if (num1) {
        nums1[i] = num1;
        m--;
    } else if(num2) {
        nums1[i] = num2;
        n--;
    }

    i--;
}


};