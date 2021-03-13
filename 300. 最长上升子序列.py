class Solution:
    def lengthOfLIS(self, nums) -> int:
        import bisect
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                loc = bisect.bisect_left(d, n)
                d[loc] = n
        return len(d)


# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。


# class Solution:
#     def lengthOfLIS(self, nums) -> int:
#         d = []
#         for n in nums:
#             if not d or n > d[-1]:
#                 d.append(n)
#             else:
#                 l, r = 0, len(d) - 1
#                 loc = r
#                 while l <= r:
#                     mid = (l + r) // 2
#                     if d[mid] >= n:
#                         loc = mid
#                         r = mid - 1
#                     else:
#                         l = mid + 1
#                 d[loc] = n
#         return len(d)
