# ref: https://discuss.leetcode.com/topic/52921/5-liner-in-python-dp-84ms


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp, maxL = [0] * len(s), 0
        for i in xrange(1, len(s)):
            if s[i] == ')':
                j = i - 1 - dp[i - 1]
                if j >= 0 and s[j] == '(':
                    # if dp[j] and dp[i] are '(' and ')'
                    dp[i] = dp[i - 1] + 2
                    if j - 1 >= 0:
                        # dp[0...i] = dp[0...j-1] + dp[j...i]
                        dp[i] += dp[j - 1]
                    maxL = max(maxL, dp[i])
        return maxL

if __name__ == '__main__':
    sol = Solution()
    print sol.longestValidParentheses(')()())')
