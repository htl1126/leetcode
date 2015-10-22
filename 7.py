import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        (sign, x) = (1, x) if x >= 0 else (-1, abs(x))
        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x /= 10
        ans *= sign
        return 0 if ans > 2147483647 or ans < -2147483648 else ans

if __name__ == '__main__':
    sol = Solution()
    print sol.reverse(int(sys.argv[1]))
