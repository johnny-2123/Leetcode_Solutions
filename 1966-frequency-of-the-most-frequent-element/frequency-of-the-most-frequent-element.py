class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq = 0
        total = 0
        left, right = 0, 0

        while right < len(nums):
            total += nums[right]
            windowLen = right - left + 1

            while total + k < nums[right] * windowLen:
                total -= nums[left]
                left += 1
                windowLen = right - left + 1

            maxFreq = max(maxFreq, windowLen)
            right += 1

        return maxFreq