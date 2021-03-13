class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        p = len(primes)
        nums = [1]
        L = [0] * p
        for i in range(1, n):
            ugly = min(nums[L[j]] * primes[j] for j in range(p))
            for j in range(p):
                if nums[L[j]] * primes[j] == ugly:
                    L[j] += 1
            nums += [ugly]
        return nums[-1]


# 编写一段程序来查找第 n 个超级丑数。
# 超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
