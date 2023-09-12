class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        curLen = 1

        for num in nums:
            if num - 1 in numSet:
                continue
            
            nextNum = num + 1
            while nextNum in numSet:
                curLen += 1
                nextNum += 1
            
            maxLength = max(maxLength, curLen)
            curLen = 1
        return maxLength