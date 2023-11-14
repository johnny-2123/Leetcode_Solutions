class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIdx, tIdx = 0, 0

        while tIdx < len(t) and sIdx < len(s):
            if t[tIdx] == s[sIdx]:
                sIdx += 1
                tIdx += 1
            else:
                tIdx += 1
        return sIdx >= len(s)