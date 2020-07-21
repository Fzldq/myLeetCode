class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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
