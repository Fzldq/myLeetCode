class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return []
        st, cur, res = [], root, []
        while st or cur:
            while cur:
                st.append(cur)
                res.append(cur.val)
                cur = cur.left
            cur = st.pop()
            cur = cur.right
        return res
