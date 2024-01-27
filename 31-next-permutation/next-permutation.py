class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivotIdx = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivotIdx = i - 1
                break
        
        if pivotIdx == -1:
            nums.sort()
            return

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[pivotIdx]:
                nums[i], nums[pivotIdx] = nums[pivotIdx], nums[i]
                break
        
        nums[pivotIdx + 1:] =  reversed(nums[pivotIdx + 1:])
        return