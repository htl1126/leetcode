# Ref: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/730567/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        return min(a - b for a, b in zip(heapq.nlargest(4, nums), heapq.nsmallest(4, nums)[::-1]))
