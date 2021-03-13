class Solution:
    def getMaxMatrix(self, matrix):
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * C for _ in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(C):
                dp[i][j] = dp[i - 1][j] + matrix[i - 1][j]
        res = (0, 0, 0, 0)
        maxSum = matrix[0][0]
        for i in range(R):
            for j in range(i, R):
                cur = k = 0
                for l in range(C):
                    if cur < 0:
                        cur = dp[j + 1][l] - dp[i][l]
                        k = l
                    else:
                        cur += dp[j + 1][l] - dp[i][l]
                    if cur > maxSum:
                        maxSum = cur
                        res = (i, k, j, l)
        return res


# 输入
# [[9, -8, 1, 3, -2],
#  [-3, 7, 6, -2, 4],
#  [6, -4, -4, 8, -7]]

# 输出
# [0,0,2,3]
