# Ref: https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/discuss/1776745/Python-Backtracking-w-set

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.ans, seen = float('inf'), set()
        def helper(steps):
            pos = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and ('r', i) not in seen and ('c', j) not in seen:
                        pos.append((i, j))
            # no new grids to be flipped, update the optimal solution
            if not pos:
                self.ans = min(self.ans, steps)
            for i, j in pos:
                seen.add(('r', i))
                seen.add(('c', j))
                helper(steps + 1)
                seen.remove(('r', i))
                seen.remove(('c', j))
        helper(0)
        return self.ans
