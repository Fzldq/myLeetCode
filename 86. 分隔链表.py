class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        before = before_head = ListNode(0)  # 02143252 02143252 021252 02122
        after = after_head = ListNode(0)  # 043252 043252 04352
        while head:
            if head.val < x:
                before.next = head  # 02143252 2143252 1252 22
                before = before.next  # 2143252 143252 252 2
            else:
                after.next = head  # 043252 43252 352
                after = after.next  # 43252 3252 52
            head = head.next  # 143252 43252 3252 252 52 2

        after.next = None  # 0435
        before.next = after_head.next  # 2122435
        return before_head.next


# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
# 输入: head = 2->1->4->3->2->5->2, x = 3
# 输出: 2->1->2->2->4->3->5
