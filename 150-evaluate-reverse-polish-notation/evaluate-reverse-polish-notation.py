class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num1 + num2
                stack.append(res)
            elif char == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 - num1
                stack.append(res)
            elif char == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 * num1
                stack.append(res)
            elif char == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2 / num1)
                stack.append(res)
            else:
                stack.append(int(char))

        return stack[0]