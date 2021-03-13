class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        days = len(prices)
        a, b, c = -prices[0], 0, 0
        for i in range(1, days):
            a, b, c = max(a, c - prices[i]), a + prices[i], max(b, c)
        return max(b, c)
