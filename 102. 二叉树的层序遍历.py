class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            tmp_cur = []
            tmp_lst = []
            for i in cur:
                tmp_cur.append(i.val)
                if i.left:
                    tmp_lst.append(i.left)
                if i.right:
                    tmp_lst.append(i.right)
            res += [tmp_cur]
            cur = tmp_lst
        return res
