# Ref: https://leetcode.com/problems/find-the-winner-of-the-circular-game/discuss/1490558/Python-Simulation-Solution-Clean-and-Concise

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n + 1)]
        last_idx = 0
        while len(circle) > 1:
            last_idx = (last_idx + k - 1) % len(circle)
            circle.pop(last_idx)
        return circle[0]
