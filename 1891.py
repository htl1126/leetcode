# Ref: https://leetcode.com/problems/cutting-ribbons/discuss/1267140/Python-Binary-Search

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0
        l, r = 1, max(ribbons)
        while l < r:
            # if we set m = (l + r) // 2, we could probably get into
            # an infinite loop when we keep going to "l = m" for case [9, 7, 5], 3
            m = (l + r + 1) // 2  # ceil((l + r) // 2) = (l + r + 1) // 2
            pieces = sum(i // m for i in ribbons)
            if pieces < k:
                r = m - 1
            else:
                l = m
        return l
