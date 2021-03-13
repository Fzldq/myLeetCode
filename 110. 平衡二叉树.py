class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True

        def height(root):
            if not self.res:
                return -1
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if abs(leftHeight - rightHeight) > 1:
                self.res = False
                return -1
            return max(leftHeight, rightHeight) + 1
        height(root)
        return self.res
