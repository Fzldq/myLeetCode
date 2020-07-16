class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
