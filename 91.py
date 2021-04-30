class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] + [0] * len(s)
        for i in range(len(s)):
            if 1 <= int(s[i]) <= 9:
                dp[i + 1] += dp[i]
            if i - 1 >= 0 and 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.numDecodings('12')
