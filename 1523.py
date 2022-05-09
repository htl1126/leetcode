# Ref: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/discuss/754726/JavaC%2B%2BPython-1-Lines

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
