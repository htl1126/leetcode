# ref: https://leetcode.com/discuss/109570/48ms-python-concise-solution
import collections


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_of_hits = 0
        self.time_hits = collections.deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.time_hits or self.time_hits[-1][0] != timestamp:
            self.time_hits.append([timestamp, 1])
        else:
            self.time_hits[-1][1] += 1
        self.num_of_hits += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.time_hits and self.time_hits[0][0] <= timestamp - 300:
            self.num_of_hits -= self.time_hits.popleft()[1]
        return self.num_of_hits

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

if __name__ == '__main__':
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    print obj.getHits(4)
    obj.hit(300)
    print obj.getHits(300)
    print obj.getHits(301)
