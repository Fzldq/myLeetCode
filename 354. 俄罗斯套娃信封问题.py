class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        n = len(envelopes)
        if not n:
            return 0
        import bisect
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        d = []
        for n in [i[1] for i in envelopes]:
            if not d or n > d[-1]:
                d.append(n)
            else:
                loc = bisect.bisect_left(d, n)
                d[loc] = n
        return len(d)


# 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
