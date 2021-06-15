# Ref: https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/discuss/1248560/Simple-Math-Problem-with-intuition-explained-O(1)-time-O(1)-space-or-Python

class Solution:
    def twoEggDrop(self, n: int) -> int:
        a, b, c = 1, 1, -2 * n  # solve x^2 + x -2n <= 0
        x = (-b + (b * b - 4 * a * c) ** 0.5) / 2
        return math.ceil(x)
