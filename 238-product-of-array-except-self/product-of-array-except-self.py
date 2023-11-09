class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [nums[0]]
        for i in range(1,len(nums)):
            num = nums[i]
            products.append(num * products[i - 1])


        reversedProducts = [nums[-1]]
        for i in range(len(nums) - 1, 0, -1):
            num = nums[i - 1]
            reversedProducts.append(num * reversedProducts[-1])


        reversedProducts.reverse()


        res = []
        for i in range(0, len(nums)):
            num1 = products[i - 1] if i > 0 else 1
            num2 = reversedProducts[i + 1] if i < len(nums) - 1 else 1
            res.append(num1 * num2)
        return res



