class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def check(root, lower, upper):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return check(root.left, lower, root.val) and check(root.right, root.val, upper)

        def count(root):
            if not root:
                return 0
            return 1 + count(root.left) + count(root.right)

        def helper(root):
            if not root:
                return
            if check(root, float('-inf'), float('inf')):
                self.res = max(self.res, count(root))
            else:
                helper(root.left)
                helper(root.right)

        helper(root)
        return self.res
