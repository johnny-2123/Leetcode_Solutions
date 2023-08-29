class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = arr[len(arr) - 1]

        for i in range(len(arr) - 1, -1, -1):
            currNum = arr[i]
            arr[i] = maxNum
            maxNum = max(currNum, maxNum)

        arr[len(arr) - 1] = -1

        return arr
