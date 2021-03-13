class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        1 2 1 2 3 4 5 5
          1 0 1 2 3 4 4
            1 2 3 4 5 4
              1 2 3 4 5
                1 2 3 4
                  1 2 3
                    1 2
                      1
        """
        from collections import defaultdict
        mod = 10 ** 9 + 7
        res = 0
        n = len(s)
        index = defaultdict(lambda: [-1])
        for idx, i in enumerate(s):
            index[i].append(idx)

        for cur_set in index.values():
            cur_set += [n]
            for i in range(1, len(cur_set) - 1):
                res += (cur_set[i] - cur_set[i - 1]) * (cur_set[i + 1] - cur_set[i])

        return res % mod


# 我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。
# 例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，
# 因为它们只出现一次，所以 countUniqueChars(s) = 5 。
# 本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。
# 注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串
# （也就是说，你必须统计 s 的所有子字符串中的唯一字符）。
# 由于答案可能非常大，请将结果 mod 10 ^ 9 + 7 后再返回。
# 输入：s = "LEETCODE"
# 输出：92
