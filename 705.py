# Ref: https://leetcode.com/problems/design-hashset/discuss/768659/Python-Easy-Multiplicative-Hash-explained

class MyHashSet:

    def __init__(self):
        self.arr = [[] for _ in range(1 << 15)]  # set() is slower for unknown reason

    def add(self, key: int) -> None:
        t = self.evalhash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.evalhash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.evalhash(key)
        return key in self.arr[t]

    def evalhash(self, key: int) -> int:
        return ((key*1031237) & (1 << 20) - 1) >> 5
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
