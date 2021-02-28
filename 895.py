# Ref: https://leetcode.com/problems/maximum-frequency-stack/discuss/163410/C%2B%2BJavaPython-O(1)

import collections

class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.m = collections.defaultdict(list)
        self.maxf = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.maxf = max(self.maxf, self.freq[x])
        self.m[self.maxf].append(x)

    def pop(self) -> int:
        x = self.m[self.maxf].pop()
        if not self.m[self.maxf]:
            self.maxf -= 1
        self.freq[x] -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

if __name__ == "__main__":
    stack = FreqStack()
    stack.push(5)
    stack.push(7)
    stack.push(5)
    stack.push(7)
    stack.push(4)
    stack.push(5)
    print(stack.freq)
    print(stack.maxf)
    print(stack.m)
    print(stack.pop())
    print(stack.freq)
    print(stack.maxf)
    print(stack.m)
    print(stack.pop())
