class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if not m * n:
            return m + n
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                leftdown = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    leftdown += 1
                dp[i][j] = min(left, down, leftdown)
        return dp[-1][-1]


# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
