class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * (k + 1)
        self.front = 0
        self.rear = 0
        self.size = k + 1

    def enQueue(self, value: int) -> bool:
        next_idx = (self.front + 1) % self.size
        if next_idx == self.rear:
            return False
        self.queue[next_idx] = value
        self.front = next_idx
        return True

    def deQueue(self) -> bool:
        if self.rear == self.front:
            return False
        self.rear = (self.rear + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear + 1) % self.size]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        if (self.front + 1) % self.size == self.rear:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
