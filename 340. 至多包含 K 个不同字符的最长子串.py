class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k:
            return n
        from collections import defaultdict
        dic = defaultdict(int)
        start = 0
        res = 0
        for cur in range(n):
            dic[s[cur]] += 1
            while len(dic) > k:
                dic[s[start]] -= 1
                if dic[s[start]] == 0:
                    del dic[s[start]]
                start += 1
            res = max(res, cur - start + 1)
        return res
