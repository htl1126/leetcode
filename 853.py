# Ref: https://leetcode.com/problems/car-fleet/discuss/255589/Python-Code-with-Explanations-and-Visualization-Beats-95

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                cur = t
                res += 1
        return res
