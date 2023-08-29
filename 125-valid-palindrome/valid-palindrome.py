class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCaseS = s.lower()
        trimmedS = "".join(char for char in lowerCaseS if char.isalnum())
        left, right = 0, len(trimmedS) - 1

        while left < len(trimmedS):
            leftChar = trimmedS[left]
            rightChar = trimmedS[right]

            if leftChar != rightChar:
                return False
            
            left += 1
            right -= 1

        return True