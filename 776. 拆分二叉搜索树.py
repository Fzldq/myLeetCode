class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def splitBST(self, root: TreeNode, V: int):
        if not root:
            return None, None
        if root.val <= V:
            bns = self.splitBST(root.right, V)
            root.right = bns[0]
            return root, bns[1]
        else:
            bns = self.splitBST(root.left, V)
            root.left = bns[1]
            return bns[0], root


# 给你一棵二叉搜索树（BST）、它的根结点 root 以及目标值 V。
# 请将该树按要求拆分为两个子树：
# 其中一个子树结点的值都必须小于等于给定的目标值 V；
# 另一个子树结点的值都必须大于目标值 V；
# 树中并非一定要存在值为 V 的结点。
# 除此之外，树中大部分结构都需要保留，
# 也就是说原始树中父节点 P 的任意子节点 C，
# 假如拆分后它们仍在同一个子树中，
# 那么结点 P 应仍为 C 的子结点。

# 输入：root = [4,2,6,1,3,5,7], V = 2
# 输出：[[2,1],[4,3,6,null,null,5,7]]
# 解释：
# 注意根结点 output[0] 和 output[1] 都是 TreeNode 对象，不是数组。

# 给定的树 [4,2,6,1,3,5,7] 可化为如下示意图：

#           4
#         /   \
#       2      6
#      / \    / \
#     1   3  5   7

# 输出的示意图如下：

#           4
#         /   \
#       3      6       和    2
#             / \           /
#            5   7         1
