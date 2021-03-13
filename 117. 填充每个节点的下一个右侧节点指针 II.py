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
        dummy, cur = Node(), root
        while cur:
            tail = dummy
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = dummy.next
            if tail == dummy:
                break
        return root


# 给定一个二叉树,
# 填充它的每个 next 指针,
# 让这个指针指向其下一个右侧节点。
# 如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 你只能使用常量级额外空间。
