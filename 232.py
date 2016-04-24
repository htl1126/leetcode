# ref: https://leetcode.com/discuss/62014/share-my-python-solution-32ms


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.in_stack, self.out_stack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.out_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack

    def move(self):
        """
        :rtype nothing
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    print queue.in_stack, queue.out_stack
    queue.push(2)
    print queue.in_stack, queue.out_stack
    queue.peek()
    print queue.in_stack, queue.out_stack
    queue.push(3)
    print queue.in_stack, queue.out_stack
    queue.peek()
    print queue.in_stack, queue.out_stack
