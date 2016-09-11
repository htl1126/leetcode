class Solution(object):
    def integerReplacement(self, n, counter=0):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        else:
            if n & 1:
                return 1 + min(self.integerReplacement(n + 1, counter + 1),
                               self.integerReplacement(n - 1, counter - 1))
            else:
                return 1 + self.integerReplacement(n / 2, counter + 1)
