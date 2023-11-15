class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLength = float("infinity")
        res = ""

        tChars = {}
        for char in t:
            tChars[char] = tChars.get(char, 0) + 1
        
        need = len(tChars.keys())
        have = 0

        start = 0
        window = {}

        for end, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in tChars and window[char] == tChars[char]:
                have += 1

            while have >= need:
                minLength = min(minLength, end - start + 1)
                if minLength == (end - start + 1): 
                    res = s[start: end + 1]

                startChar = s[start]
                window[startChar] -= 1

                if startChar in tChars and window[startChar] < tChars[startChar]:
                    have -= 1
                    
                start += 1
        
        return res