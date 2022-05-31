# Ref: https://leetcode.com/problems/meeting-scheduler/discuss/408506/JavaPython-3-simple-code-using-PriorityQueueheapq-w-brief-explanation-and-analysis

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        intervals = list(filter(lambda s: s[1] - s[0] >= duration, slots1 + slots2))
        heapq.heapify(intervals)
        while len(intervals) > 1:
            if heapq.heappop(intervals)[1] >= intervals[0][0] + duration:
                return [intervals[0][0], intervals[0][0] + duration]
        return []
