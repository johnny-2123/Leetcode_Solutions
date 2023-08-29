class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        numSet = set(nums)
        usedNums = set()

        for num in nums:
            if num - 1 in numSet:
                continue

            currLength = 1
            nextNum = num + 1
            while(nextNum in numSet):
                currLength += 1
                nextNum += 1

            maxLength = max(maxLength, currLength)
            currLength = 1
        
        return maxLength
            

            