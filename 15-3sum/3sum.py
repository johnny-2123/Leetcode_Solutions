class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    sortedNums = sorted(nums)

    res = []
    for i in range(len(sortedNums) - 2):
      num1 = sortedNums[i]
      if i > 0 and num1 == sortedNums[i -1]:
        continue
      
      left = i + 1
      right = len(sortedNums) - 1

      subseen = set()

      while left < right:
        num2 = sortedNums[left]
        num3 = sortedNums[right]
        total = num1 + num2 + num3

        if(total == 0 and not(num2 in subseen and num3 in subseen)):
          subseen.add(num2)
          subseen.add(num3)
          res.append([num1, num2, num3])
        elif total < 0:
          left += 1
        else:
          right -= 1
    
    return res