class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = ''
        end = n - 1
        while end >= 0:
            if s[end] != ' ':
                if res != '':
                    res += ' '
                start = end
                while start >= 0 and s[start] != ' ':
                    start -= 1
                res += s[start + 1:end + 1]
                end = start
            end -= 1
        return res


# 输入: "the sky is blue"
# 输出: "blue is sky the"
