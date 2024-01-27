class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)
        minAbs = float("inf")

        for i in range(len(nums) - 1):
            num1, num2 = nums[i], nums[i + 1]
            minAbs = min(minAbs, abs(num1 - num2))
        
        res = []

        for i in range(len(nums) - 1):
            num1, num2 = nums[i], nums[i + 1]
            if (abs(num1 - num2) == minAbs):
                res.append([num1, num2])
        
        return res