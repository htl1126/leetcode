# Ref: https://leetcode.com/problems/longest-repeating-substring/discuss/429950/Python-DP-solution-with-explanations-and-follow-up

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        if not s:
            return 0
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        ans, n = 0, len(s)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # dp[i][j] is the max length of repeating characters ending at s[i - 1] and s[j - 1]
                dp[i][j] = dp[i - 1][j - 1] + 1 if s[i - 1] == s[j - 1] else 0
                ans = max(ans, dp[i][j])
        return ans
