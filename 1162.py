# Ref: https://leetcode.com/problems/as-far-from-land-as-possible/discuss/360960/Python-BFS

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        if len(q) == 0 or len(q) == n * n:
            return -1
        level = 0
        while q:
            new = []
            for i, j in q:
                for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    if 0 <= i + x < n and 0 <= j + y < n and grid[i + x][j + y] == 0:
                        new.append((i + x, j + y))
                        grid[i + x][j + y] = 1
            q = new
            level += 1
        return level - 1
