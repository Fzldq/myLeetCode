class Solution:
    def updateBoard(self, board, click):
        i, j = click
        m, n = len(board), len(board[0])
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        def cal(i, j):
            res = 0
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0:
                        continue
                    if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == "M":
                        res += 1
            return res

        def dfs(i, j):
            cnt = cal(i, j)
            if cnt:
                board[i][j] = str(cnt)
                return
            board[i][j] = 'B'
            for dx in [1, -1, 0]:
                for dy in [1, -1, 0]:
                    if dx == 0 and dy == 0:
                        continue
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 'E':
                        dfs(x, y)

        dfs(i, j)
        return board


# 输入:

# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]

# Click : [3,0]

# 输出:

# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
