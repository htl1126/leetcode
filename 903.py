# Ref: https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168278/C%2B%2BJavaPython-DP-Solution-O(N2)

class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[0][i] = 1
        for i in range(n):
            cur = 0
            if s[i] == 'I':
                for j in range(n - i):
                    cur += dp[i][j]
                    dp[i + 1][j] += cur
            else:
                for j in range(n - i - 1, -1, -1):
                    cur += dp[i][j + 1]
                    dp[i + 1][j] += cur
        return dp[-1][0] % (10 ** 9 + 7)
