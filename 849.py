# Ref: https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/137912/JavaC%2B%2BPython-One-pass-Easy-Understood

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans, pre, n = 0, -1, len(seats)
        for i in range(len(seats)):
            if seats[i]:
                ans = max(ans, i if pre < 0 else (i - pre) // 2)
                pre = i
        return max(ans, n - 1 - pre)
