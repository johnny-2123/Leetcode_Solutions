class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        breakpoint = k % length
        if breakpoint == 0:
            return

        arr1 = nums[length - breakpoint:]
        arr2 = nums[:length - breakpoint]
        nums[0:0+len(arr1)] = arr1
        nums[breakpoint: breakpoint + (len(arr2))] = arr2

        
        