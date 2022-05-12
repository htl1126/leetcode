class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        row_max, col_max = [-1] * r, [-1] * c
        for i in range(r):
            for j in range(c):
                v = grid[i][j]
                row_max[i] = max(row_max[i], v)
                col_max[j] = max(col_max[j], v)
        ans = 0
        for i in range(r):
            for j in range(c):
                ans += max(0, min(row_max[i], col_max[j]) - grid[i][j])
        return ans
