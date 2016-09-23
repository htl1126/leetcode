# ref: https://discuss.leetcode.com/topic/26169/clean-java-dp-solution-with
#              -comment


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        if k >= n / 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in xrange(1, n))
        dp = [[0] * n for _ in xrange(k + 1)]
        for i in xrange(1, k + 1):
            lmax = dp[i - 1][0] - prices[0]
            for j in xrange(1, n):
                dp[i][j] = max(dp[i][j - 1], lmax + prices[j])
                lmax = max(lmax, dp[i - 1][j] - prices[j])
        return dp[-1][-1]
