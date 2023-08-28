class Solution(object):
    def twoSum(self, nums, target):
        numsSet = {}

        for i, num in enumerate(nums):
            numsSet[num] = i
            
        for i, num in enumerate(nums):
            complement = target - num
            if (complement in numsSet):
                complementIdx = numsSet[complement]
                if (complementIdx != i):
                    return [i, complementIdx]

        return None