class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        queue = list(filter(lambda i: len(graph[i]) == 1, range(n)))
        while n > 2:
            tmp = []
            while queue:
                x = queue.pop()
                y = graph[x].pop()
                graph[y].remove(x)
                if len(graph[y]) == 1:
                    tmp.append(y)
                n -= 1

            queue = tmp
        return queue


n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
s = Solution()
print(s.findMinHeightTrees(n, edges))
