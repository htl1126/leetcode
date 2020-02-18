# Ref: https://leetcode.com/problems/longest-string-chain/discuss/294890/C%2B%2BJavaPython-DP-Solution
# Algo: dynamic programming

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
        return max(dp.values())

if __name__ == "__main__":
    sol = Solution()
    print sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"])
