class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = 1

        while right < len(prices):
            rightPrice = prices[right]
            leftPrice = prices[left]

            profit = rightPrice - leftPrice
            maxProfit = max(maxProfit, profit)

            if rightPrice < leftPrice:
                left = right
                right += 1
            else:
                right += 1
        return maxProfit