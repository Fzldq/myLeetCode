class Solution:
    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, a, b):
        self.data_list[a], self.data_list[b] = self.data_list[b], self.data_list[a]

    def insert(self, value):
        self.data_list.append(value)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[parent][0] > self.data_list[index][0]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(index)

    def heapify(self, index=0):
        self.k = len(self.data_list)
        while True:
            minvalue_index = index
            if 2 * index + 1 < self.k and self.data_list[2 * index + 1][0] < self.data_list[minvalue_index][0]:
                minvalue_index = 2 * index + 1
            if 2 * index + 2 < self.k and self.data_list[2 * index + 2][0] < self.data_list[minvalue_index][0]:
                minvalue_index = 2 * index + 2
            if minvalue_index == index:
                break
            self.swap(index, minvalue_index)
            index = minvalue_index

    def heappop(self):
        remove_data, self.data_list[0] = self.data_list[0], self.data_list[-1]
        self.data_list.pop()
        self.heapify()
        return remove_data

    def heappushpop(self, value, index=0):
        if self.data_list[0][0] >= value[0]:
            return
        self.data_list[0] = value
        self.heapify()

    def trapRainWater(self, heightMap) -> int:
        if not heightMap:
            return 0

        self.data_list = []
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            self.insert((heightMap[i][0], (i, 0)))
            self.insert((heightMap[i][n - 1], (i, n - 1)))
            visited[i][0] = True
            visited[i][n - 1] = True
        for j in range(n):
            self.insert((heightMap[0][j], (0, j)))
            self.insert((heightMap[m - 1][j], (m - 1, j)))
            visited[0][j] = True
            visited[m - 1][j] = True
        direction = (0, 1, 0, -1, 0)
        res = 0
        while self.data_list:
            i, j = self.heappop()[1]
            for k in range(4):
                di, dj = i + direction[k], j + direction[k + 1]
                if 0 <= di < m and 0 <= dj < n and not visited[di][dj]:
                    if heightMap[di][dj] <= heightMap[i][j]:
                        res += heightMap[i][j] - heightMap[di][dj]
                        heightMap[di][dj] = heightMap[i][j]
                    visited[di][dj] = True
                    self.insert((heightMap[di][dj], (di, dj)))
        return res
