class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        left, right = [], []
        minp = float('inf')
        maxleft = 0
        for i in prices:
            if i < minp:
                minp = i
            if i - minp > maxleft:
                maxleft = i - minp
            left += [maxleft]
        maxp = float('-inf')
        maxright = 0
        for i in prices[::-1]:
            if i > maxp:
                maxp = i
            if maxp - i > maxright:
                maxright = maxp - i
            right += [maxright]
        res = max(i + j for i, j in zip(left, right[-2::-1]))
        return max(res, left[-1])


# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution:
    def maxProfit(self, prices) -> int:
        buy_1 = buy_2 = float('inf')
        pro_1 = pro_2 = 0

        for p in prices:
            buy_1 = min(buy_1, p)
            pro_1 = max(pro_1, p - buy_1)
            buy_2 = min(buy_2, p - pro_1)
            pro_2 = max(pro_2, p - buy_2)
        return pro_2
