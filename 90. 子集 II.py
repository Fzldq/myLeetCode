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
