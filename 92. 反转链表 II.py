# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode, tail: ListNode) -> ListNode:
        final = prev = tail.next
        curr = head
        while curr != final:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return tail, head

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair
        for _ in range(m - 1):
            pre = pre.next
        head = pre.next
        tail = head
        for _ in range(n - m):
            tail = tail.next
        head, tail = self.reverseList(head, tail)
        pre.next = head
        return hair.next
