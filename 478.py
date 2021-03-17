# Ref: https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/1113679/Python-Polar-coordinates-explained-with-diagrams-and-math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x, self.y, self.r = x_center, y_center, radius

    def randPoint(self) -> List[float]:
        theta = uniform(0, 2 * pi)
        R = self.r * sqrt(uniform(0, 1))
        return [self.x + R * cos(theta), self.y + R * sin(theta)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
