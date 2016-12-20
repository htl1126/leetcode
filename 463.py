class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        if not grid:
            return ans
        row, col = len(grid), len(grid[0])
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 1:
                    for (I, J) in ((i - 1, j), (i, j - 1), (i, j + 1),
                                   (i + 1, j)):
                        if 0 <= I < row and 0 <= J < col and grid[I][J] == 0:
                            ans += 1
                    ans += (i == 0) + (i == row - 1) + (j == 0) + (j == col - 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print sol.islandPerimeter(grid)
