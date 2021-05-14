# ref: https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.dic[key] = Node(key, value)
            self.add(self.dic[key])
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                k = self.head.next.key
                del self.dic[k]
                self.remove(self.head.next)
            self.dic[key] = Node(key, value)
            self.add(self.dic[key])
                
    def add(self, node) -> None:
        prev = self.tail.prev
        prev.next, node.next, node.prev, self.tail.prev = node, self.tail, prev, node

    def remove(self, node) -> None:
        prev, next_n = node.prev, node.next
        prev.next, next_n.prev = next_n, prev


if __name__ == '__main__':
    print 'h'
