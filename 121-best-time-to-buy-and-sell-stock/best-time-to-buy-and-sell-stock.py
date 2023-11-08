class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0

        for right, rightPrice in enumerate(prices):
            leftPrice = prices[left]

            currProfit = rightPrice - leftPrice
            maxProfit = max(currProfit, maxProfit)

            if leftPrice > rightPrice:
                left = right

        return maxProfit