class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        dp[0][1] = 1
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
