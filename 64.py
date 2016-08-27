class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = [[float('inf')] * (len(grid[0]) + 1)] + [[float('inf')] + row for
                                                        row in grid]
        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                if not (i == 1 and j == 1):
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + \
                        grid[i][j]
        return grid[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.minPathSum([[1, 2], [3, 4]])
