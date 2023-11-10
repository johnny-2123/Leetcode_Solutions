class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        targetIdx = -1

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = math.floor((start + end) /2)
            if (nums[mid] == target):
                targetIdx = mid
                break
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        if targetIdx == -1: return [-1, -1]

        start = end = targetIdx
        first = last = targetIdx

        while (start >= 0 and nums[start] == target):
            if nums[start] == target: first = start
            start -= 1
        
        while (end <= len(nums) - 1 and nums[end] == target):
            if (nums[end] == target): last = end
            end += 1
        return [first, last]