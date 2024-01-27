/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    let pivotIdx: number = -1;
    for (let i = nums.length - 1; i > 0; i--) {
        if (nums[i] > nums[i - 1]) {
            pivotIdx = i - 1;
            break;
        }
    }

    if (pivotIdx === -1) {
        nums = nums.sort((a, b) => a - b);
        return
    }

    for (let i = nums.length; i > 0; i--) {
        if (nums[i] > nums[pivotIdx]) {
            [nums[i], nums[pivotIdx]] = [nums[pivotIdx], nums[i]];
            break
        }
    }
    const sortedRight: number[] = nums.slice(pivotIdx + 1).sort((a, b) => a - b) 
    nums.splice(pivotIdx + 1, sortedRight.length, ...sortedRight)
    return;
    
};