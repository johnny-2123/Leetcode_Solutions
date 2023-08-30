class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        consecutiveZeros = 0

        if len(nums) == 1:
            return 1 if nums[0] == 0 else 0
        

        for i, num in enumerate(nums):
            if i == 0 and nums[i] == 0:
                consecutiveZeros += 1
                res += consecutiveZeros
            elif i > 0:
                prevNum = nums[i - 1]
                if prevNum != 0:
                    consecutiveZeros = 0
                
                if num == 0:
                    consecutiveZeros += 1
                    res += consecutiveZeros
        
        return res