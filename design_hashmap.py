class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None

class DesignHashmap:
    def __init__(self):
        self.max_depth = 1000
        self.depth = [ListNode() for _ in range(self.max_depth)]

    def hash(self, val: int) -> int:
        return val % self.max_depth

    def put(self, key: int, val: int) -> None:
        node = self.depth[self.hash(key)]
        while node and node.next:
            if node.next.key == key:
                node.next.val = val
            node = node.next
        node.next = ListNode(key=key, val=val)

    def get(self, key: int) -> int:
        node = self.depth[self.hash(key)].next
        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        node = self.depth[self.hash(key)]
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
            node = node.next