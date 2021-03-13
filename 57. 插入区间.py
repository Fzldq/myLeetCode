class Solution:
    def insert(self, intervals, newInterval):
        left, right = 0, len(intervals) - 1
        newleft = newInterval[0]
        newidx = 0
        while left <= right:
            mid = (left + right) >> 1
            if intervals[mid][0] == newleft:
                newidx = mid
                break
            elif intervals[mid][0] > newleft:
                newidx = mid
                right = mid - 1
            else:
                newidx = left = mid + 1
        intervals.insert(newidx, newInterval)
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
