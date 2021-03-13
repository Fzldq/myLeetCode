class Solution:
    def dfs(self, nums, idx, length):
        for i in range(idx, length):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            self.subset += [nums[i]]
            self.result += [self.subset[:]]
            self.dfs(nums, i + 1, length)
            self.subset.pop()

    def subsetsWithDup(self, nums):
        length = len(nums)
        if not length:
            return []
        nums.sort()
        self.subset, self.result = [], [[]]
        self.dfs(nums, 0, length)
        return self.result


# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
