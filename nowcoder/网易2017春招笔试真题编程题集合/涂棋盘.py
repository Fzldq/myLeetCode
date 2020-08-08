n, *bw = open(0).read().split()
n = int(n)


def lamp(grid):
    B = [1 if i == 'B' else 0 for i in grid[0]]
    W = [1 if i == 'W' else 0 for i in grid[0]]
    m = max(max(B), max(W))
    for j in range(1, n):
        tb = [1 if i == 'B' else 0 for i in grid[j]]
        tw = [1 if i == 'W' else 0 for i in grid[j]]
        B = [B[i] + 1 if tb[i] == 1 else 0 for i in range(n)]
        W = [W[i] + 1 if tw[i] == 1 else 0 for i in range(n)]
        m = max(m, max(B), max(W))
    return m


print(lamp(bw))
