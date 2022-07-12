# Ref: https://leetcode.com/problems/minimum-time-to-complete-trips/discuss/1802415/Python3-Java-C%2B%2B-Binary-Search-%2B-1-liner

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, min(time) * totalTrips
        while l < r:
            m = (l + r) // 2
            if sum(m // t for t in time) >= totalTrips:
                r = m
            else:
                l = m + 1
        return l
