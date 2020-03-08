# Ref: https://leetcode.com/problems/arithmetic-slices/discuss/215861/Detailed-Explanation%3A-Two-DP-Solutions
# Algo: dynamic programming

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [0 for _ in xrange(len(A))]
        ans = 0
        for i in xrange(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0
            ans += dp[i]
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.numberOfArithmeticSlices([1, 2, 3, 4])
