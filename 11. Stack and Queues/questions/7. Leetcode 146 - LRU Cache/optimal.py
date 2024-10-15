class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def addnode(self, newnode: Node):
        temp = self.head.next
        newnode.next = temp
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode

    def deletenode(self, delnode: Node):
        delprev = delnode.prev
        delnext = delnode.next
        delprev.next = delnext
        delnext.prev = delprev

    def get(self, key_: int) -> int:
        if key_ in self.m:
            resnode = self.m[key_]
            res = resnode.val
            del self.m[key_]
            self.deletenode(resnode)
            self.addnode(resnode)
            self.m[key_] = self.head.next
            return res
        return -1

    def put(self, key_: int, value: int):
        if key_ in self.m:
            existingnode = self.m[key_]
            del self.m[key_]
            self.deletenode(existingnode)
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deletenode(self.tail.prev)

        newnode = Node(key_, value)
        self.addnode(newnode)
        self.m[key_] = self.head.next
