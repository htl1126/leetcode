# Ref: https://leetcode.com/problems/min-cost-climbing-stairs/discuss/1256616/C%2B%2BPython-Simple-Bottom-up-DP-From-O(N)-to-O(1)-space-Clean-and-Concise

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
