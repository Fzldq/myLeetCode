class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left, right

    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            left1, right1 = self.expand(s, i, i)
            left2, right2 = self.expand(s, i, i + 1)
            if right1 - left1 - 1 > len(res):
                res = s[left1 + 1:right1]
            if right2 - left2 - 1 > len(res):
                res = s[left2 + 1:right2]
        return res
