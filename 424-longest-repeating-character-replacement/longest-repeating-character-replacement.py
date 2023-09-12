class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestStr = float("-inf")
        charCounter = {}
        left, right = 0, 0
        charCounter[s[right]] = 1

        while right < len(s):
            windowLen = right - left + 1
            maxCount = max(charCounter.values())
            maxChanges = windowLen - maxCount

            if maxChanges <= k:
                longestStr = max(longestStr, windowLen)
                right += 1
                print("right", right)
                if right < len(s):
                    charCounter[s[right]] = charCounter.get(s[right], 0) + 1
            else:
                charCounter[s[left]] -= 1
                left += 1
        
        return max(longestStr, 0)

        