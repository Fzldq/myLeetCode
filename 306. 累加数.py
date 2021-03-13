class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        self.res = False

        def backtrack(index, temp):
            if index == n:
                if len(temp) > 2:
                    self.res = True
                return
            for i in range(index, n):
                if self.res:
                    break
                new_value = num[index:i + 1]
                if not (new_value.startswith('0') and len(new_value) > 1):
                    if len(temp) >= 2 and int(new_value) == (temp[-1] + temp[-2]):
                        # print(temp, new_value)
                        backtrack(i + 1, temp + [int(new_value)])
                    elif len(temp) < 2:
                        backtrack(i + 1, temp + [int(new_value)])

        backtrack(0, [])
        return self.res


num = "121474836472147483648"
s = Solution()
print(s.isAdditiveNumber(num))
