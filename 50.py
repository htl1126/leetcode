# ref: https://discuss.leetcode.com/topic/15630/shortest-python-guaranteed/2
import sys


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        temp, ans = x, 1
        while n:
            if n & 1:
                ans *= temp
            n >>= 1
            temp **= 2
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.myPow(float(sys.argv[1]), int(sys.argv[2]))
