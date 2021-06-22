# Ref: https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = self.prev = None

class DLinkedList(object):
    def __init__(self):
        self.root = Node(None, None)
        self.root.next = self.root.prev = self.root
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.root.next
        node.prev = self.root
        node.next.prev = node
        self.root.next = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return None
        if not node:
            node = self.root.prev
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.node = dict()
        self.freq = collections.defaultdict(DLinkedList)
        self.minfreq = 0

    def inc_freq(self, node):
        freq = node.freq
        self.freq[freq].pop(node)
        if freq == self.minfreq and not self.freq[freq]:  # DLinkedList's __len__() will be called
            self.minfreq += 1
        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.node:
            return -1
        node = self.node[key]
        self.inc_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.node:
            node = self.node[key]
            self.inc_freq(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq[self.minfreq].pop()
                del self.node[node.key]
                self.size -= 1
            node = Node(key, value)
            self.node[key] = node
            self.size += 1
            self.freq[1].append(node)
            self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
