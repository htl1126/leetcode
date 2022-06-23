# Ref: https://leetcode.com/problems/first-unique-number/discuss/601179/Python-Simplest-dequecounter-solution

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = self.prev = None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head, self.tail = Node(), Node()
        self.head.next, self.head.prev = self.tail, None
        self.tail.next, self.tail.prev = None, self.head
        self.count = collections.defaultdict(int)
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        while self.head.next != self.tail:
            v = self.head.next.val
            if self.count[v] == 1:
                return v
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        return -1

    def add(self, value: int) -> None:
        self.count[value] += 1
        node = Node(value)
        self.tail.prev.next = node
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev = node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
