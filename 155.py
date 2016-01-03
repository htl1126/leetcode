# use two stacks
# source: 
# https://leetcode.com/discuss/52168/an-naive-python-solution-using-two-stacks-and-costing-88ms

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.min_stack == [] or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
