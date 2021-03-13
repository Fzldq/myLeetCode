class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head
        k %= n
        newtail = head
        for i in range(n - k - 1):
            newtail = newtail.next
        res = newtail.next
        newtail.next = None
        return res


# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
