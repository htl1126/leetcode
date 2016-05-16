# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) < 2:
            return True
        else:
            intervals = sorted(intervals, key=lambda x: x.start)
            for i in xrange(len(intervals) - 1):
                if intervals[i].end > intervals[i + 1].start:
                    return False
            return True

if __name__ == '__main__':
    sol = Solution()
    print sol.canAttendMeetings([Interval(0, 30), Interval(5, 10),
                                 Interval(7, 20)])
