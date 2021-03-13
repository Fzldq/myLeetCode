class Solution:
    def maximalSquare(self, matrix) -> int:
        if not (len(matrix) and len(matrix[0])):
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        res = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res = max(dp[i][j] ** 2, res)
        return res


matrix = [["0", "1", "1", "0", "1"],
          ["1", "1", "0", "1", "0"],
          ["0", "1", "1", "1", "0"],
          ["1", "1", "1", "1", "0"],
          ["1", "1", "1", "1", "1"],
          ["0", "0", "0", "0", "0"]]
s = Solution()
print(s.maximalSquare(matrix))
