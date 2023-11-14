class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVolume = 0
        left, right = 0, len(height) - 1

        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]
            currVolume = (right - left) * min(leftHeight, rightHeight)
            maxVolume = max(currVolume, maxVolume)

            if leftHeight < rightHeight:
                left += 1
            else:
                right -= 1
        
        return maxVolume