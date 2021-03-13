class Solution:
    def judgePoint24(self, nums) -> bool:
        def dfs(nums):
            n = len(nums)
            if n == 1:
                if abs(nums[0] - 24) < 1e-6:
                    return True
                return False
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    a, b = nums[i], nums[j]
                    newnums = [nums[k] for k in range(n) if i != k != j]
                    if dfs(newnums + [a + b]):
                        return True
                    elif dfs(newnums + [a - b]):
                        return True
                    elif dfs(newnums + [a * b]):
                        return True
                    elif b != 0 and dfs(newnums + [a / b]):
                        return True
            return False
        return dfs(nums)


nums = [3, 8, 3, 8]
s = Solution()
print(s.judgePoint24(nums))
