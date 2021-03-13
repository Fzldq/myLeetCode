class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        row, col = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (col + 1) for _ in range(row + 1)]
        dp[row][col - 1] = dp[row - 1][col] = 1
        print(dp)
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)
        return dp[0][0]


# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，
# 则骑士的初始健康点数至少为 7。

# -2 (K)  -3  3
# -5  -10 1
# 10  30  -5 (P)
