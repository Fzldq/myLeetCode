class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        faclst = [1]
        k -= 1
        res = ''
        nums = ['1']
        for i in range(1, n):
            faclst += [faclst[-1] * i]
            nums += str(i + 1)
        for i in range(n - 1, -1, -1):
            idx, k = divmod(k, faclst[i])
            res += nums[idx]
            del nums[idx]
        return res
