# ref: https://discuss.leetcode.com/topic/58042/c-1-line-solution-with
#              -explanation


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 if n == 1 else 2 * (1 + n / 2 - self.lastRemaining(n / 2))
