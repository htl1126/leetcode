# Ref: https://leetcode.com/problems/alphabet-board-path/discuss/345235/Python-Easy-Solution

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m = {c: [i // 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        ans = []
        for c in target:
            x, y = m[c]
            # If we want to reach 'z', we must move left and then move down.
            # On the other hand, we must move up first if we are at 'z'.
            if y < y0:
                ans.append("L" * (y0 - y))
            if x < x0:
                ans.append("U" * (x0 - x))
            if x > x0:
                ans.append("D" * (x - x0))
            if y > y0:
                ans.append("R" * (y - y0))
            ans.append('!')
            x0, y0 = x, y
        return "".join(ans)
