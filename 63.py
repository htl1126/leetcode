class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in xrange(len(obstacleGrid[0]) + 1)]
              for _ in xrange(len(obstacleGrid) + 1)]
        dp[0][1] = 1
        for i in xrange(len(obstacleGrid)):
            for j in xrange(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
