class Solution1:
    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            gs = 1
            stack = [(x, y)]
            while stack:
                i, j = stack.pop()
                if not seen[i][j] and grid[i][j] == '1':
                    seen[i][j] = group
                    if i > 0:
                        stack.append((i - 1, j))
                    if j > 0:
                        stack.append((i, j - 1))
                    if i < m - 1:
                        stack.append((i + 1, j))
                    if j < n - 1:
                        stack.append((i, j + 1))
            return gs

        seen = [[False] * n for _ in range(m)]
        group_size = {}
        group = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    seen[i][j] = True
                    continue
                if not seen[i][j]:
                    group_size[group] = dfs(i, j)
                    group += 1
        print(seen)
        return group - 1


class Solution2:
    def UF(self, m, n):
        self.count = 0
        self.parent = [-1] * (m * n)
        self.size = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.size[i * n + j] = 1
                    self.count += 1

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def get_size(self, p):
        rootP = self.find(p)
        return self.size[rootP]

    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        self.UF(m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            self.union(i * n + j, x * n + y)
        # print(self.parent, 'size:', self.size)
        return self.count


grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
s = Solution2()
print(s.numIslands(grid))
