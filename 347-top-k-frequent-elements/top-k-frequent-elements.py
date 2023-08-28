class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountSet = {}
        for n in nums:
            if (n in numCountSet):
                numCountSet[n] += 1
            else:
                numCountSet[n] = 1
        

        numCountPairs = [[count, num] for num, count in numCountSet.items()]

        sortedNumCountPairs = sorted(numCountPairs, key=lambda x:x[0])
        print(sortedNumCountPairs)

        mostKPairs = sortedNumCountPairs[-k:]
        print(mostKPairs)

        result = [num for count, num in mostKPairs]
        print(result)

        return result