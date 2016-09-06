class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        return sum(max(prices[i + 1] - prices[i], 0)
                   for i in xrange(len(prices) - 1))
