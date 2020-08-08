class Solution:
    def longestDecomposition(self, text: str) -> int:
        left, right = 0, len(text) - 1
        prep = 0
        res = 0
        while left <= right:
            if text[left] != text[right]:
                left += 1
                continue
            if left == right:
                res += 1
                break
            else:
                for i in range(prep, left):
                    if text[i] == text[right - left + i]:
                        continue
                    else:
                        left += 1
                        break
                else:
                    res += 2
                    right -= left - prep + 1
                    left += 1
                    prep = left
        return res


text = 'v1lvo'
s = Solution()
print(s.longestDecomposition(text))
