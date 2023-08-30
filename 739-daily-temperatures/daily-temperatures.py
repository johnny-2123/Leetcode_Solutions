class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, currTemp in enumerate(temperatures):
            while stack and currTemp > temperatures[stack[-1]]:
                prevIndex = stack.pop()
                res[prevIndex] = i - prevIndex
            stack.append(i)

        return res





