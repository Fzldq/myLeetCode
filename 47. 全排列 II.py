class Solution:
    def permuteUnique(self, nums):
        def backtrack(current_len=0):
            if current_len == n:
                res.append(nums[:])
                return
            backtrack(current_len + 1)
            for i in range(current_len):
                if nums[current_len] == nums[i]:
                    break
                nums[current_len], nums[i] = nums[i], nums[current_len]
                backtrack(current_len + 1)
                nums[current_len], nums[i] = nums[i], nums[current_len]
        nums.sort()
        n = len(nums)
        res = []
        backtrack()
        return res


# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

# 示例:

# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
