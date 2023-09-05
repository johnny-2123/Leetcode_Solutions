class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                currNum = nums[j]
                prevNum = nums[j - 1]

                if currNum < prevNum:
                    [nums[j], nums[j - 1]] = [nums[j - 1], nums[j]]
                else:
                    break
        