# Ref: https://leetcode.com/problems/cutting-ribbons/discuss/1267140/Python-Binary-Search

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0
        l, r = 1, max(ribbons)
        while l < r:
            m = (l + r + 1) // 2
            pieces = sum(i // m for i in ribbons)
            if pieces < k:
                r = m - 1
            else:
                l = m
        return l
