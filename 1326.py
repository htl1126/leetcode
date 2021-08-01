# ref: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484235/JavaC%2B%2BPython-Similar-to-LC1024

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i, r in enumerate(ranges):
            if r > 0:
                intervals.append([max(i - r, 0), min(i + r, n)])
                
        ans, start, end = 0, -1, 0
        for i, j in sorted(intervals):
            if end >= n or i > end:
                break
            elif start < i <= end:
                ans, start = ans + 1, end
            end = max(end, j)
        return ans if end >= n else -1
