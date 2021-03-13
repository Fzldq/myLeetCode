class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        from collections import defaultdict, deque
        dic = defaultdict(set)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            dic[b].add(a)
            indeg[a] += 1
        q = deque([u for u in range(numCourses) if not indeg[u]])
        visited = 0
        while q:
            x = q.popleft()
            visited += 1
            for y in dic[x]:
                indeg[y] -= 1
                if not indeg[y]:
                    q.append(y)

        return visited == numCourses
