# Ref: https://leetcode.com/problems/largest-time-for-given-digits/discuss/200517/Python-1-line-Check-Permutations-O(24)

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        return max(["%d%d:%d%d" % t for t in itertools.permutations(arr) if t[:2] < (2, 4) and t[2] < 6] or [""])
