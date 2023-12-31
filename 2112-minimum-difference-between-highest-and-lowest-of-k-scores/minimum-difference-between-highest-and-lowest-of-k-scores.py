class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()

        left = 0
        right = left + k - 1

        minDiff = float('inf')

        while right < len(nums):
            rightNum = nums[right]
            leftNum = nums[left]
            diff = rightNum - leftNum
            minDiff = min(minDiff, diff)
            left += 1
            right += 1

        return minDiff