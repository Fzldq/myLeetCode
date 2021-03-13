class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        from collections import deque

        def pick(k, nums):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return deque(stack[:k])

        def merge(num1, num2):
            res = []
            while num1 or num2:
                res.append(max(num1, num2).popleft())
            res.extend(num1 or num2)
            return res

        l1, l2 = len(nums1), len(nums2)
        return max(merge(pick(i, nums1), pick(k - i, nums2)) for i in range(k + 1) if i <= l1 and k - i <= l2)


# 给定长度分别为 m 和 n 的两个数组，
# 其元素由 0-9 构成，表示两个自然数各位上的数字。
# 现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，
# 要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
# 说明: 请尽可能地优化你算法的时间和空间复杂度。

# 示例 1:
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
