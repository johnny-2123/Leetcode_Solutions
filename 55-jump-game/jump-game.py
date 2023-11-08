class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0

        for i, num in enumerate(nums):
            if i > maxIdx: 
                return False

            maxIdx = max(maxIdx, i + nums[i])
            
            if maxIdx > len(nums) - 1: 
                return True

        return True