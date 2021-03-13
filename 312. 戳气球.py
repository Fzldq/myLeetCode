class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1]
        val.extend(nums + [1])
        for length in range(2, n + 2):
            for i in range(n + 2 - length):
                j = i + length
                for k in range(i + 1, j):
                    total = val[i] * val[j] * val[k]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        return dp[0][n + 1]


# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 现在要求你戳破所有的气球。如果你戳破气球 i ，
# 就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
# 这里的 left 和 right 代表和 i 相邻的两个气球的序号。
# 注意当你戳破了气球 i 后，
# 气球 left 和气球 right 就变成了相邻的气球。
# 求所能获得硬币的最大数量。
