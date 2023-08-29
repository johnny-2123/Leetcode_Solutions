class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charSet = set()
        maxLength = 0

        for right in range(len(s)):
            rightChar = s[right]
            while rightChar in charSet:
                leftChar = s[left]
                charSet.remove(leftChar)
                left += 1
            charSet.add(rightChar)
            length = (right - left) + 1
            maxLength = max(maxLength, length)

        return maxLength