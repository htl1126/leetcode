# Ref: https://leetcode.com/problems/unique-paths-iii/discuss/221946/JavaPython-Brute-Force-Backtracking

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans, m, n, x, y, empty = [0], len(grid), len(grid[0]), 0, 0, 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    empty += 1

        def dfs(i, j, empty):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] >= 0):
                return
            if grid[i][j] == 2:
                if empty == 0:
                    ans[0] += 1
                return
            grid[i][j] = -2
            dfs(i - 1, j, empty - 1)
            dfs(i, j - 1, empty - 1)
            dfs(i, j + 1, empty - 1)
            dfs(i + 1, j, empty - 1)
            grid[i][j] = 0
            
        dfs(x, y, empty)
        return ans[0]
