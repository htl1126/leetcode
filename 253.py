import heapq
# ref: https://discuss.leetcode.com/topic/25904/python-heap-solution-with-
#              comments


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        for i in intervals:
            if heap and i[0] >= heap[0]:  # cancel the first room finished using
                heapq.heappop(heap)
                heapq.heappush(heap, i[1])
            else:
                heapq.heappush(heap, i[1])
        return len(heap)

if __name__ == '__main__':
    sol = Solution()
    print sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
