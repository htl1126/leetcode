class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        return sum((tc - sc).values())
