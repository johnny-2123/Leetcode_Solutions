class Solution:
    def isValid(self, s: str) -> bool:
        matchingCloseParentheses = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for char in s: 
            if char in matchingCloseParentheses:
                stack.append(char)
            else:
                if not stack: return False
                openP = stack.pop()
                if char != matchingCloseParentheses[openP]:
                    return False

        return len(stack) == 0
