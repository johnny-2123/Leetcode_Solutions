class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        behindProducts = len(nums) * [0]
        product = 1
        for i, num in enumerate(nums):
            product  *= num
            behindProducts[i] = product
        print("behindProducts", behindProducts)

        product = 1
        aheadProducts = len(nums) * [0]
        for i in range(len(nums) - 1, - 1, -1):
            product *= nums[i]
            aheadProducts[i] = product
        print("aheadProducts", aheadProducts)

        res = len(nums) * [0]
        for i in range(0, len(nums)):
            num1 = behindProducts[i - 1] if i > 0 else 1
            num2 = aheadProducts[i + 1] if i < len(nums) - 1 else 1
            res[i] = num1 * num2

        return res