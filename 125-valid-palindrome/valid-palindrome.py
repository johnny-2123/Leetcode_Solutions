class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCaseS = s.lower()
        trimmedStr = "".join(char for char in lowerCaseS if char.isalnum())

        left, right = 0, len(trimmedStr) - 1

        while left < len(trimmedStr):
            if trimmedStr[left] != trimmedStr[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
