class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def dfs(root):
            if not root:
                return None
            left = dfs(root.left)
            right = dfs(root.right)
            if left or right or root.val:
                root.left = left
                root.right = right
                return root
            else:
                return None

        res = dfs(root)
        return res

# 输入: [1,1,0,1,1,0,1,0]
# 输出: [1,1,0,1,1,null,1]
