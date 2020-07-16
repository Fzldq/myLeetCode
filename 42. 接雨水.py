class Solution:
    def trap(self, height) -> int:
        n = len(height)
        if n < 3:
            return 0
        stack = []
        res = 0
        for idx, i in enumerate(height):

            p_deep = 0
            while stack:
                pidx, pi = stack[-1]
                if pi <= i:
                    res += (idx - pidx - 1) * (pi - p_deep)
                    p_deep = pi
                    stack.pop()
                elif pi > i:
                    res += (idx - pidx - 1) * (i - p_deep)
                    stack += [(idx, i)]
                    break
            else:
                stack += [(idx, i)]
        return res


height = [4, 2, 3]
s = Solution()
print(s.trap(height))
