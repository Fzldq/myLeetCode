class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(a, b):
            if not (a or b):
                return True
            if not (a and b):
                return False
            return a.val == b.val and check(a.left, b.right) and check(a.right, b.left)

        return check(root, root)
