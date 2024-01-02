class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProducts = [0] * len(nums)
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            rightProducts[i] = total

        leftProducts = [0] * len(nums)
        total = 1
        for i in range(len(nums)):
            total *= nums[i]
            leftProducts[i] = total
        
        res = [0] * len(nums)
        res[0] = 1 * rightProducts[1]
        res[len(nums) - 1] = leftProducts[len(nums) - 2] * 1

        for i in range(1, len(nums) - 1):
            res[i] = leftProducts[i - 1] * rightProducts[i + 1]
        
        return res