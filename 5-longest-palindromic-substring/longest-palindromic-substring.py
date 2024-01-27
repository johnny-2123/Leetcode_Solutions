class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLength = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and (s[left] == s[right]):
                currLength = right - left + 1
                if currLength > maxLength:
                    res = s[left: right + 1]
                    maxLength = currLength

                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and (s[left] == s[right]):
                currLength = right - left + 1
                if currLength > maxLength:
                    res = s[left: right + 1]
                    maxLength = currLength
                
                left -= 1
                right += 1
            
        return res