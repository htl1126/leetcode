class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c = 0, n - 1
        ans = 0
        while r < m and c >= 0:
            if grid[r][c] >= 0:
                r += 1
            else:
                ans += (m - r)
                c -= 1
        return ans
