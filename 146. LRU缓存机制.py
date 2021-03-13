class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.dic = {}

    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def insert(self, node):
        tmp = self.head.next
        self.head.next = node
        tmp.prev = node
        node.prev, node.next = self.head, tmp

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.delete(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.delete(node)
            self.insert(node)
            return
        if len(self.dic) == self.capacity:
            node = self.tail.prev
            self.delete(node)
            del self.dic[node.key]
        node = ListNode(key, value)
        self.dic[key] = node
        self.insert(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
