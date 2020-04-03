class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        visited = [[False for _ in xrange(col)] for _ in xrange(row)]
        ans = [0]
        def dfs(i, j, cur):
            if grid[i][j]:
                cur += grid[i][j]
                end = True
                for ni, nj in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                    if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] and not visited[ni][nj]:
                        end = False
                        visited[ni][nj] = True
                        dfs(ni, nj, cur)
                        visited[ni][nj] = False
                if end:
                    ans[0] = max(cur, ans[0])
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j]:
                    visited[i][j] = True
                    dfs(i, j, 0)
                    visited[i][j] = False
        return ans[0]

if __name__ == "__main__":
    sol = Solution()
    print sol.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])
