class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []
        self.res = []

        def dfs(root, cur):
            if root:
                cur += str(root.val)
                if not (root.left or root.right):
                    self.res.append(cur)
                    return
                if root.left:
                    dfs(root.left, cur + '->')
                if root.right:
                    dfs(root.right, cur + '->')

        dfs(root, '')
        return self.res
