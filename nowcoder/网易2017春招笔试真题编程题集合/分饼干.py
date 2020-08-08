k = input()
n = int(input())
dp = [1] + [0] * (n - 1)
for i in k:
    cur = [0] * n
    if i != 'X':
        i = int(i)
        for j in range(n):
            cur[(10 * j + i) % n] += dp[j]
    else:
        for j in range(n):
            for k in range(10):
                cur[(10 * j + k) % n] += dp[j]
    dp = cur
print(dp[0])
