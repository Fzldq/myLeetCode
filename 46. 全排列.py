class Solution:
    def permute(self, nums):
        def backtrack(current_len=0):
            if current_len == n:
                res.append(nums[:])
                return
            backtrack(current_len + 1)
            for i in range(current_len):
                nums[current_len], nums[i] = nums[i], nums[current_len]
                backtrack(current_len + 1)
                nums[current_len], nums[i] = nums[i], nums[current_len]
        nums.sort()
        n = len(nums)
        res = []
        backtrack()
        return res
