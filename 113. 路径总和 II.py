class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum1: int):
        if not root:
            return []
        res = []

        def traceback(root, cur):
            if not root.left and not root.right and sum(cur) + root.val == sum1:
                res.append(cur + [root.val])
                return
            if root.left:
                traceback(root.left, cur + [root.val])
            if root.right:
                traceback(root.right, cur + [root.val])
            cur = []
        traceback(root, [])
        return res


# 给定如下二叉树，以及目标和 sum = 22
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
