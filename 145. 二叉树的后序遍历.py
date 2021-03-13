class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        st, cur, res = [], root, []
        while st or cur:
            while cur:
                st.append(cur)
                res.append(cur.val)
                cur = cur.right
            cur = st.pop()
            cur = cur.left
        return res[::-1]
