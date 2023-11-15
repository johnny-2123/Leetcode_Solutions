class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      minLength = float("infinity")
      start = 0
      windowSum = 0

      for end, num in enumerate(nums):
        windowSum += num

        while windowSum >= target:
          minLength = min(minLength, end - start + 1)
          windowSum -= nums[start]
          start += 1
        
      return minLength if minLength != float("infinity") else 0
