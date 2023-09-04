class Solution:
    def trap(self, height: List[int]) -> int:
        leftArr = [0] * (len(height))
        maxLeft = 0
        for i in range(1, len(height)):
            prevHeight = height[i - 1]
            maxLeft = max(maxLeft, prevHeight)
            leftArr[i] = maxLeft
        print("leftArr", leftArr)

        rightArr = [0] * (len(height))
        maxRight = 0
        for i in range(len(height) - 2, -1, -1):
            nextHeight = height[i + 1]
            maxRight = max(maxRight, nextHeight)
            rightArr[i] = maxRight
        print("rightArr", rightArr)

        totalVolume = 0

        for i, currHeight in enumerate(height):
            minHeight = min(leftArr[i], rightArr[i])
            volume = minHeight - currHeight
            if volume > 0:
                totalVolume += volume
        return totalVolume
        