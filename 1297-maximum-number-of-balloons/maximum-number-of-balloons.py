class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCount = {}
        for char in text:
            charCount[char] = 1 + charCount.get(char, 0)
        print(charCount)
        
        charCount["l"] = charCount.get("l", 0) // 2
        charCount["o"] = charCount.get("o", 0) // 2

        return min(charCount.get("b", 0), charCount.get("a", 0), charCount.get("l", 0), charCount.get("o", 0), charCount.get("n", 0))