class Solution:
    def chaseGame(self, edges, startA: int, startB: int) -> int:
        n = len(edges)
        graph = [set() for _ in range(n + 1)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def bfs(v):  # 各点距离
            dist = [-1] * (n + 1)
            dist[v] = 0
            stack = [v]
            while stack:
                x = stack.pop()
                for y in graph[x]:
                    if dist[y] is -1:
                        dist[y] = dist[x] + 1
                        stack.append(y)
            return dist

        la, lb = bfs(startA), bfs(startB)
        if la[startB] == 1:  # 一步抓到
            return 1
        res = 1
        point = []
        for i in range(1, n + 1):
            if la[i] - lb[i] > 1:
                point.append(i)
                res = max(res, la[i])  # 能逃到的最远的点

        queue = list(filter(lambda i: len(graph[i]) == 1, range(1, n + 1)))
        while queue:  # 只留下环
            x = queue.pop()
            for i in graph[x]:
                graph[i].remove(x)
                if len(graph[i]) == 1:
                    queue.append(i)

        point = list(filter(lambda i: len(graph[i]) > 1, point))

        def dfs(u, v, size, start):
            """
            u: 前个点
            v: 当前点
            size: 判断环大小
            start: 起点
            环大小<=3则能抓到
            """
            if size == 0:
                return True
            for i in graph[v]:
                if i != u:
                    if i == start or not dfs(v, i, size - 1, start):
                        return False
            return True

        for i in point:
            if dfs(-1, i, 3, i):  # 如果存在某个能去的点，其存在的环大小>3，则永远抓不到
                return -1
        return res


input1 = [[1, 2], [2, 3], [3, 4], [4, 1], [2, 5], [5, 6]], 3, 5
input2 = [[1, 2], [2, 3], [3, 4], [4, 1]], 1, 3
s = Solution()
print(s.chaseGame(*input1))
print(s.chaseGame(*input2))

# https://leetcode-cn.com/problems/Za25hA/
