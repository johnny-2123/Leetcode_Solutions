function maxArea(height: number[]): number {
    let left: number = 0;
    let right: number = height.length - 1;

    let maxWater: number = 0;
    while (left < right) {
        const minHeight: number = Math.min(height[left], height[right]);
        const water: number = minHeight * (right - left);
        maxWater = Math.max(water, maxWater);

        if (height[left] <= height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxWater;
};