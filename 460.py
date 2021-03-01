# Ref: https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list

import collections

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
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        node.next = self.root.next
        node.prev = self.root
        node.next.prev = node
        self.root.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return None
        if not node:
            node = self.root.prev
        node.next.prev = node.prev
        node.prev.next = node.next
        self._size -= 1
        return node

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._size = 0
        self._capacity = capacity
        self._node = dict()
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0

    def _update(self, node):
        freq = node.freq
        self._freq[freq].pop(node)
        if freq == self._minfreq and not self._freq[freq]:  # DLinkedList's __len__() will be called
            self._minfreq += 1
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._node:
            return -1
        node = self._node[key]
        self._update(node)
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self._capacity == 0:
            return
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
            node = Node(key, value)
            self._node[key] = node
            self._size += 1
            self._freq[1].append(node)
            self._minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
