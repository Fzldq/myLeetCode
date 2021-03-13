class Solution:
    def __init__(self):
        self.res = []

    def binarySearch(self, nums, left, right, target):
        if right >= left:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                self.res[0] = min(mid, self.res[0])
                self.res[1] = max(mid, self.res[1])
            self.binarySearch(nums, left, mid - 1, target)
            self.binarySearch(nums, mid + 1, right, target)

    def searchRange(self, nums, target: int):
        n = len(nums)
        if not n:
            return [-1, -1]
        elif n == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        else:
            self.res = [len(nums) - 1, 0]
            left, right = 0, n - 1
            self.binarySearch(nums, left, right, target)
            if self.res == [len(nums) - 1, 0]:
                return [-1, -1]
            else:
                return self.res


# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。
# 找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。
