# Ref: https://leetcode.com/problems/palindromic-substrings/discuss/105707/Java-Python-DP-solution-based-on-longest-palindromic-substring
# Algo: dynamic programming

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        ans = 0
        dp = [[0 for _ in xrange(s_len)] for _ in xrange(s_len)]
        for i in xrange(s_len - 1, -1, -1):
            for j in xrange(i, s_len):
                dp[i][j] = s[i] == s[j] and (j - i + 1 < 3 or dp[i + 1][j - 1])
            ans += sum(dp[i])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.countSubstrings("aaa")
