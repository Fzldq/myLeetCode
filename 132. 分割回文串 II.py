class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1 or s[::-1] == s:
            return 0
        for i in range(1, n):
            if s[:i] == s[i - 1::-1] and s[i:] == s[:i - 1:-1]:
                return 1
        dp = list(range(n))
        for i in range(1, n):
            if s[:i + 1] == s[i::-1]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] for j in range(i) if s[j + 1:i + 1] == s[i:j:-1]) + 1
        return dp[-1]


# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回符合要求的最少分割次数。
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
