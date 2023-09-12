class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    for i in range(0, (len(nums) - 2)):
      num1 = nums[i]
      if i > 0 and num1 == nums[i - 1]:
        continue

      subseen = set()
      left = i + 1
      right = len(nums) - 1

      while left < right:
        num2 = nums[left]
        num3 = nums[right]
        total = num1 + num2 + num3

        if total == 0 and (not num2 in subseen) and (not num3 in subseen):
          res.append([num1, num2, num3])
          subseen.add(num2)
          subseen.add(num3)
        elif total < 0:
          left += 1
        else:
          right -= 1

    return res