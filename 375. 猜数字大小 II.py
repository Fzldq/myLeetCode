class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n):
            for i in range(n - length):
                min_res = float('inf')
                j = i + length
                for k in range(i + length // 2, j):
                    res = (k + 1) + max(dp[i][k - 1], dp[k + 1][j])
                    min_res = min(res, min_res)
                dp[i][j] = min_res
        # print(dp)
        return dp[0][-1]


s = Solution()
print(s.getMoneyAmount(10))

# 我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。
# 每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。
# 然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。
