# Ref: https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/discuss/228023/Elegant-Python-DP-Solution

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        dp = collections.defaultdict(int)
        ans, col = 0, len(M[0])
        for i in range(len(M)):
            for j in range(col):
                if M[i][j]:
                    dp[i, j, 0] = dp[i, j - 1, 0] + 1
                    dp[i, j, 1] = dp[i - 1, j, 1] + 1
                    dp[i, j, 2] = dp[i - 1, j - 1, 2] + 1
                    dp[i, j, 3] = dp[i - 1, j + 1, 3] + 1
                    ans = max(ans, dp[i, j, 0], dp[i, j, 1], dp[i, j, 2], dp[i, j, 3])
        return ans
