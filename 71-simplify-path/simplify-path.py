class Solution:
    def simplifyPath(self, path: str) -> str:
        splitPath = path.split("/")

        stack = []

        for ele in splitPath:
            if ele and not(ele == "..") and not(ele == "."):
                stack.append(ele)
            if (ele == ".." and stack):
                stack.pop()

        return f"/{'/'.join(stack)}"