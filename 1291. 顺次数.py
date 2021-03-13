class Solution:
    def sequentialDigits(self, low: int, high: int):
        from math import log
        llog = int(log(low, 10) + 0.01)
        hlog = int(log(high, 10) + 0.01)
        lst = []
        for i in range(llog, hlog + 1):
            tmp123 = sum([10 ** (i - j) * (j + 1) for j in range(i + 1)])
            tmp111 = sum([10 ** (i - j) for j in range(i + 1)])
            tmplst = [
                tmp123 + tmp111 * j for j in range(9 - i) if low <= tmp123 + tmp111 * j <= high]
            lst.extend(tmplst)
        return lst


# 我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。
# 请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。
# 输入：low = 1000, high = 13000
# 输出：[1234,2345,3456,4567,5678,6789,12345]
