class Solution:
    def longestLine(self, M) -> int:
        ans = 0
        for i, l in enumerate(M):
            horizontal = []
            vertical_new = []
            diagonal_new = []
            antidiagonal_new = []
            for j, n in enumerate(l):
                if n == 0:
                    horizontal.append(0)
                    vertical_new.append(0)
                    diagonal_new.append(0)
                    antidiagonal_new.append(0)
                else:
                    horizontal.append(horizontal[j - 1] + 1 if j > 0 else 1)
                    vertical_new.append(vertical[j] + 1 if i > 0 else 1)
                    diagonal_new.append(diagonal[j - 1] + 1 if i > 0 and j > 0 else 1)
                    antidiagonal_new.append(antidiagonal[j + 1] + 1 if i > 0 and j < len(M[0]) - 1 else 1)
                    ans = max(ans, horizontal[j])
                    ans = max(ans, vertical_new[j])
                    ans = max(ans, diagonal_new[j])
                    ans = max(ans, antidiagonal_new[j])
            vertical = vertical_new
            diagonal = diagonal_new
            antidiagonal = antidiagonal_new
        return ans


# 给定一个01矩阵 M，找到矩阵中最长的连续1线段。这条线段可以是水平的、垂直的、对角线的或者反对角线的。
