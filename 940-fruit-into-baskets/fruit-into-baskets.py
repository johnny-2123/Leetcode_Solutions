class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        seenFruits = {}
        maxFruits = 0

        while right < len(fruits):
            rightFruit = fruits[right]
            if rightFruit in seenFruits:
                seenFruits[rightFruit] += 1
            else:
                seenFruits[rightFruit] = 1
            while len(seenFruits) > 2:
                leftFruit = fruits[left]
                seenFruits[leftFruit] -= 1
                if seenFruits[leftFruit] == 0:
                    del seenFruits[leftFruit]
                left += 1
            
            windowLen = right - left + 1
            maxFruits = max(maxFruits, windowLen)
            right += 1
        return maxFruits
        