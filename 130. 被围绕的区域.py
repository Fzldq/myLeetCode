class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if not board:
        #     return board
        # m, n = len(board), len(board[0])

        # def dfs(i, j):
        #     board[i][j] = 'A'
        #     for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        #         if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
        #             dfs(x, y)

        # for j in range(n):
        #     if board[0][j] == "O":
        #         dfs(0, j)
        #     if board[m - 1][j] == "O":
        #         dfs(m - 1, j)

        # for i in range(m):
        #     if board[i][0] == "O":
        #         dfs(i, 0)
        #     if board[i][n - 1] == "O":
        #         dfs(i, n - 1)

        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             board[i][j] = 'X'
        #         if board[i][j] == 'A':
        #             board[i][j] = 'O'

        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(dummy, i * col + j)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) != find(i * col + j) and board[i][j] == "O":
                    board[i][j] = "X"


# 示例:

# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：

# X X X X
# X X X X
# X X X X
# X O X X
