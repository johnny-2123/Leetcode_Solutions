/**
 * @param {number[]} nums
 * @return {number[][]}
 */

var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    const results = [];

    for(let i = 0; i < nums.length - 2; i++) {
        const num1 = nums[i];
        if (i > 0 && num1 === nums[i - 1]) {
            continue; 
        }

        let left = i + 1;
        let right = nums.length - 1;
        
        const subSeen = new Set()
        while (left < right) {
            const num2 = nums[left];
            const num3 = nums[right];
            const total = num1 + num2 + num3;
            

            if(total === 0 && !(subSeen.has(num2) && subSeen.has(num3))) {
                subSeen.add(num2);
                subSeen.add(num3)
                results.push([num1, num2, num3])
                left++;
                right--;
            } else if (total < 0) {
                left++;
            } else {
                right--;
            }
        }

    }

    console.log(results)
    return results
};