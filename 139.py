# ref: https://leetcode.com/discuss/23605/simple-dp-
#              solution-in-python-with-description


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True
        dp = [False for _ in xrange(len(s))]
        for i in xrange(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1: i + 1] and (dp[i - len(w)]
                                                      or i - len(w) == -1):
                    dp[i] = True
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.wordBreak('leetcode', ['leet', 'code'])
