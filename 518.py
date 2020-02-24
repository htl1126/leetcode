# Ref: https://leetcode.com/problems/coin-change-2/discuss/99210/python-O(n)-space-dp-solution
# Algo: dynamic programming

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0 for _ in xrange(amount)]
        for coin in coins:
            for i in xrange(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.change(5, [1, 2, 5])
