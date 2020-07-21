# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
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
