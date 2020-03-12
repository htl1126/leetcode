# Ref: https://leetcode.com/problems/longest-arithmetic-sequence/discuss/274611/JavaC%2B%2BPython-DP
# Algo: dynamic programming

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = {}
        for i in xrange(len(A)):
            for j in xrange(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())

if __name__ == "__main__":
    sol = Solution()
    print sol.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8])
