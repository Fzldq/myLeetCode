class Solution:
    def isUgly(self, num: int) -> bool:
        factor = [2, 3, 5]
        if num <= 0:
            return False
        while num > 1:
            flag = 0
            for i in factor:
                if num % i == 0:
                    num = num / i
                else:
                    flag += 1
            if flag == 3:
                return False
        return True


# 编写一个程序判断给定的数是否为丑数。
# 丑数就是只包含质因数 2, 3, 5 的正整数。
