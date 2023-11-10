class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      lastLength = 0
      currLength = 0

      for char in s:
        if char != " ":
          currLength += 1
          lastLength = currLength
        else:
          currLength = 0
      
      return lastLength