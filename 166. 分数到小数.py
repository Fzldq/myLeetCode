class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        div, numerator = divmod(numerator, denominator)
        res.append(str(div))
        if numerator == 0:
            return ''.join(res)
        res.append('.')
        dic = {(div, numerator): len(res)}
        while numerator:
            numerator *= 10
            div, numerator = divmod(numerator, denominator)

            if (div, numerator) in dic:
                res.insert(dic[(div, numerator)], '(')
                res.append(')')
                break
            dic[(div, numerator)] = len(res)
            res.append(str(div))
        return ''.join(res)


# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 输入: 7, -12
# 输出: "-0.58(3)"
