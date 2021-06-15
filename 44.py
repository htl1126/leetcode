# ref: https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(len(p)):
            if p[j] == '*':
                dp[0][j + 1] = True
            else:
                break

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] in {s[i], '?'}:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j]  # '*' is for multiple chars or an empty string
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch('aa', 'a*')
