import heapq
# ref: https://discuss.leetcode.com/topic/25904/python-heap-solution-with-
#              comments


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.start)
        heap = []
        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heapreplace(heap, i.end)
            else:
                heapq.heappush(heap, i.end)
        return len(heap)

if __name__ == '__main__':
    sol = Solution()
    print sol.minMeetingRooms([Interval(0, 30), Interval(5, 10),
                               Interval(15, 20)])
