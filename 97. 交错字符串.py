class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, k):
            if i == m and j == n:
                return True
            if i > m or j > n:
                return False
            if i < m and s1[i] == s3[k] and dfs(i + 1, j, k + 1):
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j + 1, k + 1):
                return True
            return False
        return dfs(0, 0, 0)
