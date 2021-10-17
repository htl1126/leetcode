# ref: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/discuss/1525309/JavaC%2B%2BPython-DP-solution

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.Counter([0])
        for n in nums:
            for k, v in dp.items():
                dp[k | n] = dp[k | n] + v  # should use v instead of dp[k] to avoid using newly updated values
        return dp[max(dp)]
