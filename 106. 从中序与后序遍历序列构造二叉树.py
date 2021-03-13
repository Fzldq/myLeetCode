class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        length = len(inorder)
        dic = {inorder[i]: i for i in range(length)}

        def build(inleft, inright, poleft, poright):
            if poleft > poright or inleft > inright:
                return None
            rootval = postorder[poright]
            pIndex = dic[rootval]
            root = TreeNode(rootval)
            root.left = build(inleft, pIndex - 1, poleft,
                              poleft + pIndex - inleft - 1)
            root.right = build(pIndex + 1, inright, poleft + pIndex - inleft, poright - 1)
            return root
        return build(0, length - 1, 0, length - 1)
