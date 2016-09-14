class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.pos_len = [[0, len(v1)], [0, len(v2)]]
        self.cur = 0
        self.data = [v1, v2]
        if self.pos_len[self.cur][0] >= self.pos_len[self.cur][1]:
            self.cur = 1 - self.cur

    def next(self):
        """
        :rtype: int
        """
        ret = self.data[self.cur][self.pos_len[self.cur][0]]
        self.pos_len[self.cur][0] += 1
        self.cur = 1 - self.cur
        if self.pos_len[self.cur][0] >= self.pos_len[self.cur][1]:
            self.cur = 1 - self.cur
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos_len[self.cur][0] < self.pos_len[self.cur][1]

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
