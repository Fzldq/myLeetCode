class Solution:
    def subsets(self, nums):
        res = []
        n = 1 << len(nums)
        for i in range(n):
            cur = i
            cur_lst = []
            cur_idx = 0
            while cur:
                if cur & 1:
                    cur_lst += [nums[cur_idx]]
                cur_idx += 1
                cur >>= 1
            res += [cur_lst]
        return res


# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
