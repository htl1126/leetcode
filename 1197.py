# Ref: https://leetcode.com/problems/minimum-knight-moves/discuss/387120/Python3-Clear-short-and-easy-DP-solution-No-Need-for-BFS-or-math

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        memo = {}
        def DP(x, y):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2
            if (x, y) not in memo:
                memo[(x, y)] = min(DP(abs(x - 2), abs(y - 1)), DP(abs(x - 1), abs(y - 2))) + 1
            return memo[(x, y)]
        return DP(abs(x), abs(y))
