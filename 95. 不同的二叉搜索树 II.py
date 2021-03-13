class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):

        def helper(left, right):
            if left > right:
                return [None]
            res = []
            for i in range(left, right + 1):
                lefttree = helper(left, i - 1)
                righttree = helper(i + 1, right)
                for a in lefttree:
                    for b in righttree:
                        cur = TreeNode(i)
                        cur.left = a
                        cur.right = b
                        res += [cur]
            return res
        return helper(1, n) if n else []
