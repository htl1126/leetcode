# Ref: https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/835323/Python-3-or-DP-or-Explanation

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_len, dp, count = 0, [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            max_len = max(max_len, dp[i])
        return sum(c for size, c in zip(dp, count) if size == max_len)
