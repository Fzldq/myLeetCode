class Solution:
    def exist(self, board, word: str) -> bool:
        if not (len(board) and len(board[0])):
            return False
        m, n = len(board), len(board[0])
        lw = len(word)
        if m * n < len(word):
            return False
        dp = [[True] * n for _ in range(m)]
        res = False

        def dfs(i, j, cur, res):
            if res:
                return res
            if dp[i][j] and board[i][j] == word[cur]:
                if cur == lw - 1:
                    return True
                dp[i][j] = False
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ni < m and 0 <= nj < n:
                        res |= dfs(ni, nj, cur + 1, res)
                dp[i][j] = True
            else:
                return False
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res |= dfs(i, j, 0, res)
                    if res:
                        break
        return res


# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
