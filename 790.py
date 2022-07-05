# Ref: https://leetcode.com/problems/domino-and-tromino-tiling/discuss/1620975/C%2B%2BPython-Simple-Solution-w-Images-and-Explanation-or-Optimization-from-Brute-Force-to-DP

class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0, 0] for _ in range(n + 2)]  # if n == 1, we need to use n + 2 not n + 1
        dp[1], dp[2] = [1, 1], [2, 2]
        for i in range(3, n + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 2][1]
            dp[i][1] = dp[i - 1][0] + dp[i - 1][1]
        return dp[n][0] % (10 ** 9 + 7)
