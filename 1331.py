# ref: https://leetcode.com/problems/rank-transform-of-an-array/discuss/489753/JavaC%2B%2BPython-HashMap

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for n in sorted(arr):
            rank.setdefault(n, len(rank) + 1)
        return map(rank.get, arr)
