class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0

        for i in range(0, len(nums)):
            if i > maxIdx:
                return False
            
            maxIdx = max(maxIdx, i + nums[i])

            if maxIdx > len(nums) - 1:
                return True
        
        return True
