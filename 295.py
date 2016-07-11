# ref: https://discuss.leetcode.com/topic/27521/short-simple-java-c-
#              python-o-log-n-o-1/2
from heapq import heappush, heappushpop, heappop


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print mf.findMedian()
    mf.addNum(3)
    print mf.findMedian()
