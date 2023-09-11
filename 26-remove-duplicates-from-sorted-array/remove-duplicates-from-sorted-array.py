class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        j = 0

        for i in range(1, len(nums)):
            prevNum = nums[i - 1]
            currNum = nums[i]

            if prevNum != currNum:
                j += 1
                nums[j] = nums[i]

        return j + 1