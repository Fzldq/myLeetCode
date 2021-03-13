# 和84一个道理

class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(m):
            if i == 0:
                max_h = [int(j) for j in matrix[0]]
            else:
                max_h = [(max_h[j] + 1) * int(matrix[i][j]) for j in range(n)]

            left = [0] * n
            right = [n] * n
            queue = []
            for j in range(n):
                while queue and max_h[j] <= max_h[queue[-1]]:
                    right[queue[-1]] = j
                    queue.pop()
                left[j] = queue[-1] if queue else -1
                queue.append(j)

            res += [max((right[j] - left[j] - 1) * max_h[j] for j in range(n))]
        return max(res)


# 输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6
