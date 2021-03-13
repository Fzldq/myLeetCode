class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                cost[i][j] = cost[i + 1][j - 1] + (0 if s[i] == s[j] else 1)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                if j == 1:
                    dp[i][j] = cost[0][i - 1]
                else:
                    dp[i][j] = min(dp[i0][j - 1] + cost[i0][i - 1] for i0 in range(j - 1, i))

        return dp[-1][-1]


# 给你一个由小写字母组成的字符串 s，和一个整数 k。

# 请你按下面的要求分割字符串：

# 首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
# 接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
# 请返回以这种方式分割字符串所需修改的最少字符数。

# 示例 1：
# 输入：s = "abc", k = 2
# 输出：1
# 解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。
