class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [-1] + [0] * (k - 1)
        self.front = self.rear = 0
        self.size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            if not self.isInitState():
                self.front = (self.front + 1) % self.size
            self.deque[self.front] = value
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            if not self.isInitState():
                self.rear = (self.rear - 1) % self.size
            self.deque[self.rear] = value
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            if self.front == self.rear:
                self.deque[self.front] = -1
            else:
                self.front = (self.front - 1) % self.size
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            if self.front == self.rear:
                self.deque[self.rear] = -1
            else:
                self.rear = (self.rear + 1) % self.size
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.rear == self.front and self.deque[self.rear] == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size > 1 and (self.front + 1) % self.size == self.rear or self.size == 1 and self.deque[self.front] != -1
    
    def isInitState(self) -> bool:
        return self.front == self.rear and self.deque[self.front] == -1


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
