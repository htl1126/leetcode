# Ref: https://leetcode.com/problems/rle-iterator/discuss/168286/JavaPython-3-straightforward-code-with-comment-O(n)-time-and-O(1)-extra-space

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.data, self.index = encoding, 0

    def next(self, n: int) -> int:
        while self.index < len(self.data):
            if n <= self.data[self.index]:
                self.data[self.index] -= n
                return self.data[self.index + 1]
            n -= self.data[self.index]
            self.index += 2
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
