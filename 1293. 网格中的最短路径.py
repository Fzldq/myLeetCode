class Solution:
    def shortestPath(self, grid, k: int) -> int:
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        if m == n == 1:
            return 0
        if k >= m + n - 3:
            return m + n - 2
        state = (0, 0, k)
        queue = deque([(state, 0)])
        marked = [[-1] * n for _ in range(m)]
        while queue:
            (i, j, k), steps = queue.popleft()
            steps += 1
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n:
                    state = (x, y, k - grid[x][y])
                    if state[2] <= marked[x][y]:
                        continue
                    if x == m - 1 and y == n - 1:
                        return steps
                    marked[x][y] = state[2]
                    queue.append((state, steps))
        return -1


# 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。
# 每一步，您都可以在空白单元格中上、下、左、右移动。
# 如果您最多可以消除k个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径,
# 并返回通过该路径所需的步数。
# 如果找不到这样的路径，则返回 -1。

grid = [[0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]]
k = 1
s = Solution()
print(s.shortestPath(grid, k))
