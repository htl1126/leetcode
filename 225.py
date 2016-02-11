# source: https://leetcode.com/discuss/41728/python-solution-o-1-o-n-for-push-48ms

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = collections.deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        for i in xrange(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
        self.stack.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
