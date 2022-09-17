# Ref: https://leetcode.com/problems/design-most-recently-used-queue/discuss/1066079/Python3-summarizing-3-approaches

class MRUQueue:

    def __init__(self, n: int):
        self.n = n
        self.sqrt_n = int(sqrt(n))
        self.index = []  # the first number in self.data[i] is the (self.index[i])'th in the queue
        self.data = []
        for i in range(1, n + 1):
            idx = (i - 1) // self.sqrt_n
            if idx == len(self.data):
                self.data.append([])
                self.index.append(i)
            self.data[-1].append(i)

    def fetch(self, k: int) -> int:
        i = bisect.bisect_right(self.index, k) - 1  # find the smallest i such that self.index[i] > k
        x = self.data[i].pop(k - self.index[i])
        for j in range(i + 1, len(self.index)):
            self.index[j] -= 1
        if len(self.data[-1]) == self.sqrt_n:
            self.data.append([])
            self.index.append(self.n)
        self.data[-1].append(x)
        if self.data[i] == []:
            self.data.pop(i)
            self.index.pop(i)
        return x


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
