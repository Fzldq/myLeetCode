class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not (len(grid) and len(grid[0])):
            return 0
        row, col = len(grid), len(grid[0])
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.res = 0

        def dfs(i, j):
            grid[i][j] = 0
            res = 1
            for di, dj in move:
                ci, cj = i + di, j + dj
                if 0 <= ci < row and 0 <= cj < col and grid[ci][cj]:
                    res += dfs(ci, cj)
            self.res = max(res, self.res)
            return res

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    dfs(i, j)
        return self.res


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

s = Solution()
print(s.maxAreaOfIsland(grid))
