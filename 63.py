class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == [[]]:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        table = [[0 for _ in xrange(col + 1)] for _ in xrange(row + 1)]
        table[0][1] = 1
        for i in xrange(1, row + 1):
            for j in xrange(1, col + 1):
                if obstacleGrid[i - 1][j - 1] == 0:
                    table[i][j] = table[i][j - 1] + table[i - 1][j]
        return table[row][col]

if __name__ == '__main__':
    sol = Solution()
    print sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
