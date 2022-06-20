# Ref: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/286705/JavaC%2B%2BPython-DP

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[k] * values[j] for k in range(i + 1, j))
        return dp[0][-1]
