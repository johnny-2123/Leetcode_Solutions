class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left, right, = 0, 1

        while right < len(prices):
            leftNum = prices[left]
            rightNum = prices[right]
            profit = rightNum - leftNum
            maxProfit = max(maxProfit, profit)
            if(rightNum < leftNum):
                left = right
                right += 1
            else:
                right += 1
        return maxProfit
            