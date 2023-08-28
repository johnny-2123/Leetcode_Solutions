/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    nums.sort();

    const trackedNums = {}

    let numCount = 1;
    for(let idx = 1; idx <= nums.length; idx++) {
        const currNum = nums[idx];
        const prevNum = nums[idx - 1];
        
        if(currNum === prevNum) {
            numCount += 1;
        } else {
            trackedNums[numCount] = trackedNums[numCount] || [];
            trackedNums[numCount].push(prevNum)
            numCount = 1;
        }
    } 


    
    let mostFrequentKeys = Object.keys(trackedNums).sort((a, b) => a -b).slice(-k)

    const mostFrequentNums = [];

    for (let i = 0; i < mostFrequentKeys.length; i++) {
        const key = mostFrequentKeys[i]
        mostFrequentNums.push(...trackedNums[key])
    }

    return mostFrequentNums.slice(-k)

};