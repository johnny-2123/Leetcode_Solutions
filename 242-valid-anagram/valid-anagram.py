class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if(len(s) != len(t)):
            return False

        sSortedArr = sorted(s)
        sSorted = "".join(sSortedArr)
        tSortedArr = sorted(t)
        tSorted = "".join(tSortedArr)

        print(sSorted)
        print(tSorted)

        for i in range(len(s)):
            sChar = sSorted[i]
            tChar = tSorted[i]
            print(i)
            print(sChar)
            print(tChar)
            if tChar != sChar:
                return False


        return True