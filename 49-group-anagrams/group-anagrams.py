class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedStrs = {}

        for s in strs:
            alphabetizedStr = "".join(sorted(s))
            if(alphabetizedStr in groupedStrs):
                groupedStrs[alphabetizedStr].append(s)
            else:
                groupedStrs[alphabetizedStr] = [s]

        return groupedStrs.values()