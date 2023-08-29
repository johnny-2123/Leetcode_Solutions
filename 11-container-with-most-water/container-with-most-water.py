class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = float("-inf")
        left = 0
        right = len(height) - 1

        while left < right:
            leftHeight = height[left]
            rightHeight = height[right] 
            width = right - left

            currArea = min(leftHeight, rightHeight) * width

            maxArea = max(maxArea, currArea)

            if(leftHeight < rightHeight):
                left += 1
            else:
                right -= 1
        return maxArea