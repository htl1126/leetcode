class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        self.nonisland = False
        row, col = len(grid), len(grid[0])
        if not (row > 2 and col > 2):
            return 0
        visited = [[False for _ in range(col)] for _ in range(row)]
        def dfs(i, j):
            visited[i][j] = True
            for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                if (x in [0, row - 1] or y in [0, col - 1]) and grid[x][y] == 0:
                    self.nonisland = True
                if 0 < x < row - 1 and 0 < y < col - 1 and not visited[x][y] and grid[x][y] == 0:
                    dfs(x, y)
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if not visited[i][j] and grid[i][j] == 0:
                    self.nonisland = False
                    dfs(i, j)
                    if not self.nonisland:
                        ans += 1
        return ans
