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

        mostKPairs = sortedNumCountPairs[-k:]

        result = [num for count, num in mostKPairs]

        return result