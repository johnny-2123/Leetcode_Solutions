from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        print("numCount", numCount)
        countNumPairs = [(count, num) for num, count in numCount.items()]
        countNumPairs.sort(reverse=True)
        print("countNumPairs", countNumPairs)
        result = []
        i = 0
        while i < k:
            num = countNumPairs[i][1]
            result.append(num)
            i += 1
        return result
