class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        subset = ""

        def _backtrack(openCount, closeCount):
            nonlocal subset
            if openCount == n and closeCount == n:
                ans.append(subset)
                return
            
            if openCount < n:
                subset += "("
                _backtrack(openCount + 1, closeCount)
                subset = subset[:-1]
            
            if closeCount < openCount:
                subset += ")"
                _backtrack(openCount, closeCount + 1)
                subset = subset[:-1]
        _backtrack(0, 0)
        return ans
        