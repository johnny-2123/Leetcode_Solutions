class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        steps = 0

        while right < len(nums) - 1:
            maxIdx = 0
            for i in range(left, right + 1):
                maxIdx = max(maxIdx, i + nums[i])
            left = right + 1
            right = maxIdx
            steps += 1
        
        return steps