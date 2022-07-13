# Ref: https://leetcode.com/problems/number-of-people-aware-of-a-secret/discuss/2229982/JavaC%2B%2BPython-Sliding-window-O(n)-Time-O(forget)-Space

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [1] + [0] * (n - 1)
        mod = 10 ** 9 + 7
        share = 0
        for i in range(1, n):
            share = (share + dp[i - delay] - dp[i - forget]) % mod
            dp[i] = share
        return sum(dp[-forget:]) % mod
