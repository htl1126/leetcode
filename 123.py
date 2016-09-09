# ref: https://discuss.leetcode.com/topic/4766/a-clean-dp-solution-which
#              -generalizes-to-k-transactions


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0] * len(prices) for _ in xrange(3)]
        maxprofit = 0
        for k in xrange(2):
            max1 = dp[k - 1][0] - prices[0]
            for i in xrange(1, len(prices)):
                dp[k][i] = max(dp[k][i - 1], prices[i] + max1)
                max1 = max(max1, dp[k - 1][i] - prices[i])
                maxprofit = max(dp[k][i], maxprofit)
        return maxprofit

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProfit([3, 2, 1, 5, 7])
