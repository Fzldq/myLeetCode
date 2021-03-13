class Solution:
    def spiralOrder(self, matrix):
        res = []
        if not len(matrix):
            return res
        row, col = len(matrix), len(matrix[0])
        grid = [[0] * col for _ in range(row)]

        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        direct = 0
        dx, dy = move[direct % 4]
        while True:
            if grid[x][y]:
                break
            res += [matrix[x][y]]
            grid[x][y] = 1
            if not (0 <= x + dx < row and 0 <= y + dy < col) or grid[x + dx][y + dy]:
                direct += 1
                dx, dy = move[direct % 4]
            if 0 <= x + dx < row and 0 <= y + dy < col:
                x += dx
                y += dy
        return res


# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
