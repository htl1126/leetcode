# Ref: https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/471601/Clean-DP-solution-with-explanation
# Ref: https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/446088/Python-DP-with-explaination
# Algo: Dynamic Programming
import sys

class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        num_pile = len(stones)
        if (num_pile - 1) % (K - 1):
            return -1
        acc_sum = [0 for _ in xrange(num_pile + 1)]
        for i in xrange(num_pile):
            acc_sum[i + 1] = acc_sum[i] + stones[i]
        dp = [[0 for _ in xrange(num_pile + 1)] for _ in xrange(num_pile + 1)]

        for L in xrange(K, num_pile + 1):
            i = 0
            j = i + L - 1
            while j < num_pile:
                dp[i][j] = sys.maxint
                for k in xrange(i, j, K - 1):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                if (L - 1) % (K - 1) == 0:
                    dp[i][j] += acc_sum[j + 1] - acc_sum[i]
                i += 1
                j += 1
        return dp[0][num_pile - 1]

if __name__ == "__main__":
    sol = Solution()
    print sol.mergeStones([3, 2, 4, 1], 3)
