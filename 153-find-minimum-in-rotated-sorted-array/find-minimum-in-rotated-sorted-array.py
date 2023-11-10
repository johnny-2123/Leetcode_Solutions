class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = math.floor((left + right) / 2)
            leftNum = nums[left]
            rightNum = nums[right]
            midNum = nums[mid]

            if leftNum <= rightNum:
                return leftNum
            elif leftNum <= midNum:
                left = mid + 1
            else:
                right = mid
        return nums[left]