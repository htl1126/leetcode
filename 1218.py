# Ref: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/discuss/398216/Python-4-lines

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for n in arr:
            dp[n] = dp[n - difference] + 1 if n - difference in dp else 1
        return max(dp.values())
