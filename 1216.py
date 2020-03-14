# Ref: https://leetcode.com/problems/valid-palindrome-iii/discuss/397606/Find-Longest-Palindromic-Subsequence.
# Algo: dynamic programming

class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        s_len = len(s)
        dp = [[0 for _ in xrange(s_len)] for _ in xrange(s_len)]
        for i in xrange(s_len - 1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i + 1, s_len):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1] >= s_len - k
        
if __name__ == "__main__":
    sol = Solution()
    print sol.isValidPalindrome("abcdeca", 2)
