class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not (len(matrix) and len(matrix[0])):
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False


# 在一个 n * m 的二维数组中，
# 每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。
