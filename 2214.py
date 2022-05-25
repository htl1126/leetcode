# Ref: https://leetcode.com/problems/minimum-health-to-beat-game/discuss/1883509/Python-Easy-to-understand-beats-88-runtime-and-36-memory

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return 1 + sum(damage) - min(max(damage), armor)
