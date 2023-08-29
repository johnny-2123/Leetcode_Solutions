class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        for i, row in enumerate(wall):
            total = 0
            for k, width in enumerate(row):
                if k == len(row) - 1:
                    continue
                total += width
                wall[i][k] = total

        frequencyCount = {}
        for i, row in enumerate(wall):
            if len(row) == 1:
                continue
            for k, total in enumerate(row):
                if k == len(row) - 1:
                    continue
                frequencyCount[total] = 1 + frequencyCount.get(total, 0)
        
        maxFrequency = 0
        for count in frequencyCount.values():
            maxFrequency = max(maxFrequency, count)

        return len(wall) - maxFrequency
