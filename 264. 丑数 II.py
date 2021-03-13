class Ugly:
    def __init__(self):
        nums = [1]
        i2 = i3 = i5 = 0
        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
            nums += [ugly]
        self.nums = nums


class Solution:
    u = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n - 1]


# 编写一个程序，找出第 n 个丑数。
# 丑数就是质因数只包含 2, 3, 5 的正整数。
