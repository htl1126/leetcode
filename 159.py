# ref: https://discuss.leetcode.com/topic/11739/clean-11-lines-ac-answer-o-1
#              -space-o-n-time
# Follow-up: how about three distinct?


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j, maxlen = 0, -1, 0
        for k in xrange(1, len(s)):
            if s[k] != s[k - 1]:
                if j >= 0 and s[k] != s[j]:
                    maxlen = max(maxlen, k - i)
                    i = j + 1  # the new begin position for the new sequence
                j = k - 1
        return maxlen if maxlen > len(s) - i else len(s) - i  # case 'eebbeee'


if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLongestSubstringTwoDistinct('abc')
