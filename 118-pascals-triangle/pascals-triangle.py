class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range (1, numRows):
            arr = []
            prevArr = res[i - 1]
            j = 0

            while j <= i:
                num1 = prevArr[j - 1] if 0 <= (j - 1) < len(prevArr) else 0
                num2 = prevArr[j] if 0 <= j < len(prevArr) else 0
                arr.append(num1 + num2)
                j += 1
            res.append(arr)
        return res
            