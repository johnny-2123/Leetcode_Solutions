function minimumAbsDifference(arr: number[]): number[][] {
    const nums: number[] = arr.sort((a, b) => a - b);
    let minAbs: number = Infinity;

    for (let i = 0; i < nums.length - 1; i++) {
        const num1 = nums[i];
        const num2 = nums[i + 1];
        minAbs = Math.min(minAbs, Math.abs(num1 - num2));
    }

    const res: number[][] = [];

    for (let i = 0; i < nums.length - 1; i++) {
        const num1 = nums[i];
        const num2 = nums[i + 1];
        
        if (Math.abs(num1 - num2) === minAbs) res.push([num1, num2])
    }

    return res;
};