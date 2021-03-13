class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        inordersequence = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            inordersequence.append(root.val)
            if root.right:
                inorder(root.right)

        def build(left, right):
            if left > right:
                return None
            mid = (left + right) >> 1
            cur = TreeNode(inordersequence[mid])
            cur.left = build(left, mid - 1)
            cur.right = build(mid + 1, right)
            return cur

        inorder(root)
        return build(0, len(inordersequence) - 1)


# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，
# 新生成的树应该与原来的树有着相同的节点值。
# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，
# 我们就称这棵二叉搜索树是 平衡的 。
# 如果有多种构造方法，请你返回任意一种。

# 输入：root = [1,null,2,null,3,null,4,null,null]
# 输出：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
