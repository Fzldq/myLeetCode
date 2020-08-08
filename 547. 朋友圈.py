# DFS
class Solution1:
    def findCircleNum(self, M) -> int:
        n = len(M)
        if n <= 1:
            return n

        def dfs(i):
            gs = 1
            stack = [i]
            seen[i] = group
            while stack:
                x = stack.pop()
                for idx, y in enumerate(M[x]):
                    if y and not seen[idx]:
                        seen[idx] = group
                        gs += 1
                        stack += [idx]
            return gs

        seen = [False] * (n + 1)
        group_size = {}
        group = 1
        for i in range(n):
            if not seen[i]:
                group_size[group] = dfs(i)
                group += 1
        return group - 1


# 并查集
class Solution2:
    def UF(self, n):
        self.count = n
        self.parent = [0] * n
        self.size = [1] * n
        for i in range(n):
            self.parent[i] = i

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

    def findCircleNum(self, M) -> int:
        n = len(M)
        self.UF(n)
        for i in range(n):
            for j in range(i):
                if M[i][j]:
                    self.union(i, j)
        print(self.size)
        return self.count


M = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]
s = Solution2()
print(s.findCircleNum(M))
