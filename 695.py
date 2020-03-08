class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area, self.cur_area = 0, 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        def dfs(i, j):
            visited[i][j] = True
            self.cur_area += 1
            for ni, nj in ((i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j)):
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] and not visited[ni][nj]:
                    dfs(ni, nj)
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] and not visited[i][j]:
                    self.cur_area = 0
                    dfs(i, j)
                    if self.cur_area > max_area:
                        max_area = self.cur_area
        return max_area

if __name__ == "__main__":
    sol = Solution()
    print sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
