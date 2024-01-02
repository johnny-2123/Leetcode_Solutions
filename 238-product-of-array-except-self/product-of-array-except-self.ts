function productExceptSelf(nums: number[]): number[] {
    const rightProducts: number[] = [];
    let total: number = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        total *= nums[i];
        rightProducts[i] = total;
    }

    const leftProducts: number[] = [];
    total = 1;
    for (let i = 0; i < nums.length; i++) {
        total *= nums[i];
        leftProducts[i] = total;
    }
    
    const res: number[] = [];
    res[0] = 1 * rightProducts[1];
    res[nums.length - 1] = leftProducts[nums.length - 2] * 1;

    for (let i = 1; i < nums.length - 1; i++) {
        res[i] = leftProducts[i - 1] * rightProducts[i + 1]; 
    }

    return res;
};