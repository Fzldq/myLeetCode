class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        cur = root
        while cur.left:
            head = cur
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            cur = cur.left
        return root


# 给定一个完美二叉树,
# 填充它的每个 next 指针,
# 让这个指针指向其下一个右侧节点。
# 如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 你只能使用常量级额外空间。
