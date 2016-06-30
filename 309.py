# ref: https://leetcode.com/discuss/71391/easiest-java-solution-with
#              -explanations


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        b0 = -prices[0]
        b1 = b0
        s0, s1, s2 = 0, 0, 0
        for i in xrange(1, len(prices)):
            b0 = max(b1, s2 - prices[i])
            s0 = max(s1, b1 + prices[i])
            b1 = b0
            s2 = s1
            s1 = s0
        return s0

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProfit([1, 2, 3, 0, 2])
