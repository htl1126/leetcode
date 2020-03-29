# Ref: https://leetcode.com/problems/super-egg-drop/discuss/443089/Python-DP-Solution-with-Detailed-Explanation
# Algo: dynamic programming

class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        m = 300
        dp = [[0 for _ in xrange(K + 1)] for _ in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, K + 1):
                dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
                if dp[i][j] >= N:
                    return i

if __name__ == "__main__":
    sol = Solution()
    print sol.superEggDrop(2, 6)
