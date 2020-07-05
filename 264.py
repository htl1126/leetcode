class Solution(object):
    ugly = sorted(2 ** a * 3 ** b * 5 ** c for a in xrange(32) for b in xrange(20) for c in xrange(14))
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ugly[n - 1] 

if __name__ == '__main__':
    sol = Solution()
    print sol.nthUglyNumber(6)
