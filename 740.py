# Ref: https://leetcode.com/problems/delete-and-earn/discuss/109871/Awesome-Python-4-liner-with-explanation-Reduce-to-House-Robbers-Question-U0001f31d

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        point = [0] * 10001
        for n in nums:
            point[n] += n
        pre = cur = 0
        for v in point:
            # for v at point[i], pre = dp[i - 2], cur = dp[i - 1]
            # we want to get dp[-1]
            pre, cur = cur, max(pre + v, cur)
        return cur
