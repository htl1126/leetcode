# Ref: https://leetcode.com/problems/coloring-a-border/discuss/282839/Python-BFS-and-DFS

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        seen, m, n = set(), len(grid), len(grid[0])
        
        def dfs(x, y):
            if (x, y) in seen:
                return True
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == grid[row][col]):
                return False
            seen.add((x, y))
            if dfs(x - 1, y) + dfs(x, y - 1) + dfs(x, y + 1) + dfs(x + 1, y) < 4:
                grid[x][y] = color
            return True
        dfs(row, col)
        return grid
