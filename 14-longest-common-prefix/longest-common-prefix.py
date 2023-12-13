class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs[0]: return ""

        prefix = strs[0]
        
        for s in strs:
            newPrefix = ""
            idx = 0
            
            while (idx < len(s)) and (idx < len(prefix)) and (s[idx] == prefix[idx]):
                newPrefix += s[idx]
                idx += 1
            prefix = newPrefix
            
        return prefix