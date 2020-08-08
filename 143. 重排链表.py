class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        re_node = slow.next
        slow.next = None
        pre = None
        while re_node:
            nexttemp = re_node.next
            re_node.next = pre
            pre = re_node
            re_node = nexttemp
        hair = ListNode(-1)
        dummy = hair
        while head or pre:
            if head and pre:
                tmp1, tmp2 = head.next, pre.next
                dummy.next = head
                dummy.next.next = pre
                dummy = dummy.next.next
                head, pre = tmp1, tmp2
            else:
                dummy.next = head
                dummy = dummy.next
                head = head.next
        head = dummy.next
