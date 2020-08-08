def main():
    n, k, *num = map(int, open(0).read().split())
    num = [num]
    mul = [[0] * n for _ in range(n)]
    for i in range(n):
        if i != n - 1:
            mul[i][i] = mul[i + 1][i] = 1
        else:
            mul[i][i] = mul[0][i] = 1

    def multiply(a, b):
        row = len(a)
        res = [[sum(a[i][j] * b[j][k] for j in range(n)) %
                100 for k in range(n)] for i in range(row)]
        return res

    while k:
        if k & 1:
            num = multiply(num, mul)
        mul = multiply(mul, mul)
        k >>= 1
    print(*num[0])


if __name__ == '__main__':
    main()
