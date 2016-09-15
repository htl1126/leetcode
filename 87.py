# ref: https://discuss.leetcode.com/topic/9726/python-recursive-solution


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in xrange(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
                    f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.isScramble('great', 'rgtae')
