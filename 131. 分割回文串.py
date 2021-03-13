class Solution:
    def partition(self, s: str):
        n = len(s)
        if not n:
            return [[]]
        if n == 1:
            return [[s]]
        res = []
        for i in range(1, n + 1):
            if s[:i][::-1] == s[:i]:
                res += [[s[:i]] + j for j in self.partition(s[i:])]
        return res


# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
# 示例:
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
