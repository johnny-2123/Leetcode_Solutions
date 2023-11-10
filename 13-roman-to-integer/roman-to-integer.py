class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000  
        }

        total = 0
        prevValue = 0

        for char in s:
            currValue = values[char]

            if currValue > prevValue:
                total -= prevValue
                total += (currValue - prevValue)
            else:
                total += currValue
            
            prevValue = currValue
        return total