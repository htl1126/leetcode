import sys

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        temp = x
        result = 1
        if n == 0:
            return 1
        negative = False
        if n < 0:
            n = -n
            negative = True
        while n > 0:
            if n % 2 == 1:
                result *= temp
            temp = temp ** 2
            n /= 2
        if negative:
            return 1 / result
        else:
            return result

if __name__ == '__main__':
    sol = Solution()
    print sol.myPow(float(sys.argv[1]), int(sys.argv[2]))
