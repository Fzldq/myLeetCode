class Solution:
    def UF(self, m, n):
        self.row = m
        self.col = n
        self.count = 0
        self.parent = list(range(self.row * self.col))
        # self.size = [1] * (self.row * self.col)

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        # if self.size[rootP] > self.size[rootQ]:
        #     self.parent[rootQ] = rootP
        #     self.size[rootP] += self.size[rootQ]
        # else:
        #     self.parent[rootP] = rootQ
        #     self.size[rootQ] += self.size[rootP]
        self.parent[rootQ] = rootP
        self.count -= 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def numIslands2(self, m: int, n: int, positions):
        self.grid = [[0] * n for _ in range(m)]
        self.UF(m, n)
        self.res = [0]
        for i, j in positions:
            if not (0 <= i < self.row and 0 <= j < self.col) or self.grid[i][j] == 1:
                self.res.append(self.count)
                continue
            self.grid[i][j] = 1
            self.count += 1
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < self.row and 0 <= y < self.col and self.grid[x][y] == 1:
                    self.union(i * self.col + j, x * self.col + y)
            self.res.append(self.count)
        return self.res[1:]


# 带更新的岛屿数量
