# Ref: https://leetcode.com/problems/koko-eating-bananas/discuss/152324/JavaC%2B%2BPython-Binary-Search

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l + r ) // 2
            if sum((p + m - 1) // m for p in piles) > h:
                l = m + 1
            else:
                r = m
        return l
