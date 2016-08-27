# ref: https://discuss.leetcode.com/topic/31929/math-solution
import math


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

if __name__ == '__main__':
    sol = Solution()
    print sol.bulbSwitch(24)
