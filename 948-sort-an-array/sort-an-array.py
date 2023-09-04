class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums

        midPt = len(nums) // 2
        leftHalf = nums[0:midPt]
        rightHalf = nums[midPt:]

        return merge(self.sortArray(leftHalf), self.sortArray(rightHalf))

    def merge(leftArr, rightArr):
        res = []
        left, right = 0, 0

        while left < len(leftArr) and right < len(rightArr):
            leftVal = leftArr[left]
            rightVal = rightArr[right]

            if leftVal <= rightVal: 
                res.append(leftVal)
                left += 1
            else:
                res.append(rightVal)
                right += 1
        
        return res.append(leftArr[left:]).append(rightArr[right:])