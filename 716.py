# Ref: https://leetcode.com/problems/max-stack/discuss/309621/Python-using-stack-%2B-heap-%2B-set-with-explanation-and-discussion-of-performance

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.h = []
        self.soft_deleted = set()
        self.next_id = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.next_id))
        heapq.heappush(self.h, (-x, self.next_id))
        self.next_id -= 1

    def pop(self) -> int:
        v, i = self.stack.pop()
        self.soft_deleted.add(i)
        self.clean()
        return v

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return -self.h[0][0]

    def popMax(self) -> int:
        v, i = heapq.heappop(self.h)
        self.soft_deleted.add(i)
        self.clean()
        return -v
    
    def clean(self) -> None:
        while self.stack and self.stack[-1][1] in self.soft_deleted:
            self.soft_deleted.remove(self.stack.pop()[1])
        while self.h and self.h[0][1] in self.soft_deleted:
            self.soft_deleted.remove(heapq.heappop(self.h)[1])

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
