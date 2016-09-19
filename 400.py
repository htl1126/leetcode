# ref: https://discuss.leetcode.com/topic/59378/short-python-java


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
        for digits in xrange(1, 11):
            first = 10 ** (digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n / digits)[n % digits])
            n -= 9 * first * digits

if __name__ == '__main__':
    sol = Solution()
    print sol.findNthDigit(13)
