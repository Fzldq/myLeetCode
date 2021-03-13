class Solution:
    def wordBreak(self, s: str, wordDict):
        memo = {}

        def dfs(s, memo, wordDict):
            if s in memo:
                return memo[s]
            if s == '':
                return []
            res = []
            for word in wordDict:
                if not s.endswith(word):
                    continue
                if len(word) == len(s):
                    res.append(word)
                else:
                    rest = dfs(s[:-len(word)], memo, wordDict)
                    for item in rest:
                        item += ' ' + word
                        res.append(item)
            memo[s] = res
            return res

        return dfs(s, memo, wordDict)


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
S = Solution()
print(S.wordBreak(s, wordDict))
