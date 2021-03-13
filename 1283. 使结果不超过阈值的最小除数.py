class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        def func(x, y):
            return (x // y) + (x % y != 0)
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) >> 1
            if sum(func(i, mid) for i in nums) <= threshold:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


# 输入：nums = [1,2,5,9], threshold = 6
# 输出：5
# 解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
# 如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
