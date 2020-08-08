def main():
    n = int(input())
    lst = list(map(lambda x: int(x) >> 10, input().split()))

    s = sum(lst) // 2
    dp = [0] * (s + 1)
    for i in range(n):
        for j in range(s, -1, -1):
            if j >= lst[i]:
                tmp = dp[j - lst[i]] + lst[i]
                if dp[j] < tmp:
                    dp[j] = tmp
            else:
                break
    print(max(dp[s], sum(lst) - dp[s]) << 10)


if __name__ == '__main__':
    main()
