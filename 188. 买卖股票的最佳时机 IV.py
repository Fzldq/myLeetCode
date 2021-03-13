from typing import List
import re
f = open('188. 买卖股票的最佳时机 IV.csv')
k, *prices = map(int, re.split('[\n,]', f.read()))


class Solution:
    def maxProfit_inf(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res

    def maxProfit(self, k: int, prices: List[int]) -> int:
        day = len(prices)
        if k > day // 2:
            return self.maxProfit_inf(prices)
        buy = [float('inf')] * (k + 1)
        buy[0] = 0
        profit = [0] * (k + 1)

        for p in prices:
            for i in range(1, k + 1):
                buy[i] = min(buy[i], p - profit[i - 1])
                profit[i] = max(profit[i], p - buy[i])
        return profit[-1]


s = Solution()
print(s.maxProfit(k, prices))
