function trap(height: number[]): number {
    const leftHeight: number[] = [];
    let prevMax: number = 0;
    for (let i = 0; i < height.length; i++) {
        leftHeight[i] = prevMax;
        prevMax = Math.max(prevMax, height[i]);
    }

    const rightHeight: number[] = [];
    prevMax = 0;
    for (let i = height.length - 1; i >=0; i--) {
        rightHeight[i] = prevMax;
        prevMax = Math.max(prevMax, height[i]);
    }

    let total: number = 0;
    for (let i = 0; i < height.length; i++) {
        const minHeight: number = Math.min(leftHeight[i], rightHeight[i]);
        const currWater = minHeight - height[i];
        if (currWater > 0) total += currWater; 
    }
    return total;
};