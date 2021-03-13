class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftdepth = self.minDepth(root.left)
        rightdepth = self.minDepth(root.right)
        if not (leftdepth and rightdepth):
            return leftdepth + rightdepth + 1
        return 1 + min(leftdepth, rightdepth)
