class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1


        while left < right:
            mid = (left + right) // 2
            midNum = nums[mid]
            leftNum = nums[left]
            rightNum = nums[right]




            if leftNum <= rightNum:
                return leftNum
               
            if leftNum <= midNum:
                left = mid + 1
            else:
                right = mid
        return nums[left]