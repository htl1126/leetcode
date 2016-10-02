import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctr = collections.Counter(s)
        return sum(ctr[c] / 2 * 2 for c in ctr) + any(ctr[c] for c in ctr
                                                      if ctr[c] % 2 == 1)
