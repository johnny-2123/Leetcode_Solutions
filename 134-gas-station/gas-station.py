class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
             return -1
        
        diff = [gas[i] - cost[i] for i in range(0, len(gas))]
        
        total = 0
        res = 0
        
        for i, num in enumerate(diff):
            total += num
            
            if total < 0:
                total = 0
                res = i + 1
        return res