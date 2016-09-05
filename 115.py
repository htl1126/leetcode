# ref: https://discuss.leetcode.com/topic/51131/space-o-mn-and-o-n-python
#              -solutions


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        r, c = len(s), len(t)
        dp = [[0 for _ in xrange(c + 1)] for _ in xrange(r + 1)]
        for i in xrange(r + 1):
            dp[i][0] = 1
        for i in xrange(1, r + 1):
            for j in xrange(1, c + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (
                    s[i - 1] == t[j - 1])
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.numDistinct('rabbbit', 'rabbit')
