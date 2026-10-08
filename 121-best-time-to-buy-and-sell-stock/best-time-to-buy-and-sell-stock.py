class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buyPrice = prices[0]
        profit = 0

        for i in range(1,n):
            currPrice = prices[i]
            if buyPrice > currPrice :
                buyPrice = currPrice
            profit = max(profit, currPrice - buyPrice)
        return profit

        