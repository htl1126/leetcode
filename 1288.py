# Ref: https://leetcode.com/problems/remove-covered-intervals/discuss/451277/JavaC%2B%2BPython-Sort-Solution

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = right = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for i, j in intervals:
            ans += j > right
            right = max(right, j)
        return ans
