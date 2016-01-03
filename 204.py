# Sieve of Eratosthenes
# Source: https://leetcode.com/discuss/57717/python-o-n-log-log-n-time-and-o-n-space

import sys
import itertools

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        nums = range(1, n, 2)
        nums[0] = 0
        count = 1
        n //= 2
        for p in itertools.ifilter(None, nums):
            count += 1
            for q in xrange(p * p // 2, n, p):
                nums[q] = 0
        return count

if __name__ == '__main__':
    sol = Solution()
    print sol.countPrimes(int(sys.argv[1]))
