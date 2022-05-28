# Ref: https://leetcode.com/problems/minimum-time-difference/discuss/100637/Python-Straightforward-with-Explanation

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        t = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        t.append(t[0] + 1440)  # to compute diff between t[0] and t[-1]
        return min(b - a for a, b in zip(t, t[1:]))
