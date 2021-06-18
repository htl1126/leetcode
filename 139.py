# ref: https://leetcode.com/discuss/23605/simple-dp-
#              solution-in-python-with-description


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1: i + 1]:
                    if i - len(w) >= 0 and dp[i - len(w)] or i -len(w) + 1 == 0:
                        dp[i] = True
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.wordBreak('leetcode', ['leet', 'code'])
