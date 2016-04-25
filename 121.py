# ref:https://leetcode.com/discuss/48378/kadanes-algorithm
#             -since-mentioned-about-interviewer-twists


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        maxProfitHere = 0
        maxSoFar = 0
        for i in xrange(1, len(prices)):
            maxProfitHere = max(0,
                maxProfitHere + prices[i] - prices[i - 1])
            maxSoFar = max(maxProfitHere, maxSoFar)
        return maxSoFar
        
if __name__ == '__main__':
    sol = Solution()
    print sol.maxProfit([1, 7, 4, 11])
