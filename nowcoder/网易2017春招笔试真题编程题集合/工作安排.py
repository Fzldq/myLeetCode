from functools import reduce
n, *S = open(0).read().split()
n = int(n)
engineers = []
for s in S:
    engineers += [reduce(lambda x, y: x | y, map(lambda i: 1 << int(i), s))]


def dfs(i, engineers, cur_done):
    result = 0
    for k in range(100):
        if not engineers[i] & (1 << k):
            continue
        if not cur_done & (1 << k):
            if i == n - 1:
                result += 1
            else:
                result += dfs(i + 1, engineers, cur_done | (1 << k))
    return result


print(dfs(0, engineers, 0))
