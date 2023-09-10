class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        charSet = set()
        left = 0

        for right, rightChar in enumerate(s):
            while rightChar in charSet:
                charSet.remove(s[left])
                left += 1
            currLength = right - left + 1
            maxLength = max(maxLength, currLength)
            charSet.add(rightChar)
        
        return maxLength