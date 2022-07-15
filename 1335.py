# Ref: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/944828/Short-DP-solution-with-highly-detailed-step-by-step-explanation

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [float('inf')] * n + [0]
        for D in range(1, d + 1):
            for i in range(n - D + 1):
                maxd, dp[i] = 0, float('inf')
                for j in range(i, n - D + 1):
                    maxd = max(maxd, jobDifficulty[j])
                    dp[i] = min(dp[i], maxd + dp[j + 1])
        return dp[0]
