class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        currNum = nums[0]
        print("nums", nums)
        print("currNum", currNum)
        print("n", len(nums)/2)

        for num in nums:
            if num != currNum:
                count = 1
                currNum = num
            else:
                count += 1
            print("num", num)
            print("count", count)

            if count > (len(nums)/2):
                return currNum