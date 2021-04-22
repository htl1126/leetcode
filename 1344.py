class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = abs(6 * minutes - ((hour % 12) * 30 + 0.5 * minutes))
        return min(a, 360 - a)
