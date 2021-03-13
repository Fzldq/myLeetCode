class Solution:
    def splitIntoFibonacci(self, S: str):
        n = len(S)
        self.res = []

        def backtrack(index, temp):
            if index == n:
                if len(temp) > 2:
                    self.res = temp
                return
            for i in range(index, min(index + 10, n)):
                if self.res:
                    break
                new_value = S[index:i + 1]
                if int(new_value) > 2 ** 31 - 1:
                    break
                if not (new_value.startswith('0') and len(new_value) > 1):
                    if len(temp) >= 2 and int(new_value) == (temp[-1] + temp[-2]):
                        backtrack(i + 1, temp + [int(new_value)])
                    elif len(temp) < 2:
                        backtrack(i + 1, temp + [int(new_value)])

        backtrack(0, [])
        return self.res
