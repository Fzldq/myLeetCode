class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')

        def recursion(root):
            if not root:
                return 0
            left = max(recursion(root.left), 0)
            right = max(recursion(root.right), 0)
            cur = root.val + left + right
            self.res = max(self.res, cur)
            return root.val + max(left, right)
        recursion(root)
        return self.res
