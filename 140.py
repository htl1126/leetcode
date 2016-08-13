# ref: https://discuss.leetcode.com/topic/35762/9-lines-python-10-lines-c


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in xrange(i + 1, len(s) + 1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)

if __name__ == '__main__':
    sol = Solution()
    print sol.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
