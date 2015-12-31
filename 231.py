# bit manipulation, source: https://leetcode.com/discuss/65893/python-one-line-solution

import sys

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n - 1)

if __name__ == '__main__':
    sol = Solution()
    print sol.isPowerOfTwo(int(sys.argv[1]))
