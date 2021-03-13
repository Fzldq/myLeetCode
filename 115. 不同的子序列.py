class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        dp = [[0] * (s_len + 1) for _ in range(t_len + 1)]
        for i in range(s_len):
            dp[0][i] = 1
        for i in range(1, t_len + 1):
            for j in range(1, s_len + 1):
                dp[i][j] = dp[i][j - 1] + (dp[i - 1][j - 1] if s[j - 1] == t[i - 1] else 0)
        return dp[-1][-1]
