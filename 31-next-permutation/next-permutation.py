class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivotIdx = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                print("nums[i]", nums[i])
                print("nums[i-1]", nums[i-1])
                print("-----")
                pivotIdx = i - 1
                break
        
        if pivotIdx == -1:
            return nums.sort()

        print("nums", nums)

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[pivotIdx]:
                print("nums[i]", nums[i])
                print("nums[pivotIdx]", nums[pivotIdx])
                nums[i], nums[pivotIdx] = nums[pivotIdx], nums[i]
                break
        
        print('nums 27: ', nums)
        nums[pivotIdx + 1:] =  reversed(nums[pivotIdx + 1:])
        print("nums 29: ", nums)
        return nums