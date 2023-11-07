class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        currNum = nums[0]

        for num in nums:
            if num != currNum:
                count = 1
                currNum = num
            else:
                count += 1

            if count > (len(nums)/2):
                return currNum