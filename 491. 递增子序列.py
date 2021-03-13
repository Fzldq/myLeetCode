class Solution:
    def findSubsequences(self, nums):
        n = len(nums)
        self.res = []

        def dfs(cur, idx):
            if len(cur) > 1:
                self.res += [cur]
            if idx == n:
                return
            used = set()
            for i in range(idx, n):
                if nums[i] in used:
                    continue
                if not cur or nums[i] >= cur[-1]:
                    used |= {nums[i]}
                    dfs(cur + [nums[i]], i + 1)

        dfs([], 0)
        return self.res


# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
