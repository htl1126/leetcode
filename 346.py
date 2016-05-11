class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.size:
            self.queue = self.queue[1:]
            self.queue.append(val)
        else:
            self.queue.append(val)
        return float(sum(self.queue)) / len(self.queue)

if __name__ == '__main__':
    m = MovingAverage(3)
    print m.next(1)
    print m.next(10)
    print m.next(3)
    print m.next(5)
