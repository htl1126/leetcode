# ref: https://leetcode.com/discuss/58056/summary-of-different-
#              solutions-bfs-static-and-mathematics


import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if int(math.sqrt(n)) ** 2 == n:
            return 1
        while n & 3 == 0:
            n >>= 2
        if n & 7 == 7:
            return 4
        sqrt_n = int(math.sqrt(n))
        for i in xrange(1, sqrt_n + 1):
            if int(math.sqrt(n - i * i)) ** 2 == n - i * i:
                return 2
        return 3

if __name__ == '__main__':
    sol = Solution()
    print sol.numSquares(13)
