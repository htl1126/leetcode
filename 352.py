import itertools
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = set()
        self.addNum = self.vals.add

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        groups = [list(g) for _, g in itertools.groupby(
            enumerate(sorted(self.vals)), lambda (i, val): val - i)]
        return [[g[0][1], g[-1][1]] for g in groups]

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
