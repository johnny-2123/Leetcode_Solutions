from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        word1 = sorted(word1)
        word2 = sorted(word2)
        str1Counter = Counter(word1)
        str2Counter = Counter(word2)
        distinctCount1 = len(list(str1Counter.keys()))
        distinctCount2 = len(list(str2Counter.keys()))

        for i, char1 in enumerate(word1):
            if i > 0 and char1 == word1[i - 1]:
                continue
            for k, char2 in enumerate(word2):
                if k > 0 and char2 == word2[k -1]:
                    continue
                # take char1 out of str1
                str1Counter[char1] -= 1
                if str1Counter[char1] == 0:
                    distinctCount1 -= 1
                #add char1 to str2
                if str2Counter.get(char1, 0) > 0:
                    str2Counter[char1] += 1
                else:
                    str2Counter[char1] = 1
                    distinctCount2 += 1
                #take char2 out of str2
                str2Counter[char2] -= 1
                if str2Counter[char2] == 0:
                    distinctCount2 -= 1
                #add char2 to str1
                if str1Counter.get(char2, 0) > 0:
                    str1Counter[char2] += 1
                else:
                    str1Counter[char2] = 1
                    distinctCount1 += 1
                    
                if distinctCount1 == distinctCount2:
                    return True

                # Reverse the operations to undo the changes
                str1Counter[char1] += 1
                if str1Counter[char1] == 1:
                    distinctCount1 += 1

                str2Counter[char1] -= 1
                if str2Counter[char1] == 0:
                    distinctCount2 -= 1

                str2Counter[char2] += 1
                if str2Counter[char2] == 1:
                    distinctCount2 += 1

                str1Counter[char2] -= 1
                if str1Counter[char2] == 0:
                    distinctCount1 -= 1

        return False


        