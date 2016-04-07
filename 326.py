import sys
import math

# Math Solution https://leetcode.com/discuss/78532/summary-all-solutions
# -new-method-included-at-15-30pm-jan-8t

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            return math.log10(n) / math.log10(3) % 1 == 0
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    print sol.isPowerOfThree(int(sys.argv[1]))
