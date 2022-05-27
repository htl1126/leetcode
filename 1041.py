# Ref: https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856/JavaC%2B%2BPython-Let-Chopper-Help-Explain

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == "L":
                dx, dy = -dy, dx
            elif i == "R":
                dx, dy = dy, -dx
            else:
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
