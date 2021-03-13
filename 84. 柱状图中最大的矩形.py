class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        queue = []
        for i in range(n):
            while queue and heights[i] <= heights[queue[-1]]:
                right[queue[-1]] = i
                queue.pop()
            left[i] = queue[-1] if queue else -1
            queue.append(i)

        res = max((right[i] - left[i] - 1) * heights[i]
                  for i in range(n)) if n > 0 else 0
        return res


# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
