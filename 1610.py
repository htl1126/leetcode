# Ref: https://leetcode.com/problems/maximum-number-of-visible-points/discuss/877822/Python-clean-sliding-window-solution-with-explanation

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        extra = 0
        x0, y0 = location
        angles = []
        
        for x, y in points:
            if x == x0 and y == y0:
                extra += 1
            else:
                angles.append(math.atan2(y - y0, x - x0))
        angles.sort()
        angles = angles + [i + 2 * math.pi for i in angles]
        
        i, j = 0, 0
        ans = 0
        angle = angle * math.pi / 180
        for j in range(len(angles)):
            while angles[j] - angles[i] > angle:
                i += 1
            ans = max(ans, j - i + 1)
        return ans + extra
