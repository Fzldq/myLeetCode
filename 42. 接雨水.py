class Solution:
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        res = maxleft = maxright = 0
        left, right = 0, n - 1
        while left < right:
            if maxleft < maxright:
                if maxleft < height[left]:
                    maxleft = height[left]
                else:
                    res += maxleft - height[left]
                    left += 1
            else:
                if maxright < height[right]:
                    maxright = height[right]
                else:
                    res += maxright - height[right]
                    right -= 1
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
print(s.trap(height))
