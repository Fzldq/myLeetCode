class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        for end in range(len(s)):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end + 1]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res
