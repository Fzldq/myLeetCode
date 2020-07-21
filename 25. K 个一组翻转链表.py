# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode, tail: ListNode) -> ListNode:  # tail 345 head 12345
        final = prev = tail.next  # 45
        curr = head
        while curr != final:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            head, tail = self.reverseList(head, tail)
            pre.next = head
            pre = tail
            head = tail.next
        return hair.next
