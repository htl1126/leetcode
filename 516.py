# Ref: https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution
# Algo: dynamic programming

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        dp = [[0 for _ in xrange(s_len)] for _ in xrange(s_len)]
        for i in xrange(s_len - 1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i + 1, s_len):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][-1]
        
if __name__ == "__main__":
    sol = Solution()
    print sol.longestPalindromeSubseq("bbbab")
