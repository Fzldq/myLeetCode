class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        length = len(inorder)
        dic = {inorder[i]: i for i in range(length)}

        def build(preleft, preright, inleft, inright):
            if preleft > preright or inleft > inright:
                return None
            rootval = preorder[preleft]
            pIndex = dic[rootval]
            root = TreeNode(rootval)
            root.left = build(preleft + 1, pIndex - inleft + preleft, inleft, pIndex - 1)
            root.right = build(pIndex - inleft + preleft + 1,
                               preright, pIndex + 1, inright)
            return root
        return build(0, length - 1, 0, length - 1)
