# ref: https://leetcode.com/discuss/42344/7-lines-easy-python


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for i in sorted(intervals, key=lambda i: i.start):
            if result and result[-1].end >= i.start:
                result[-1].end = max(result[-1].end, i.end)
            else:
                result += i,
        return result

if __name__ == '__main__':
    sol = Solution()
    print sol.merge([Interval(1, 3), Interval(2, 6), Interval(8, 10),
                     Interval(15, 18)])
