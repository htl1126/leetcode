# ref: https://discuss.leetcode.com/topic/18054/4-lines-o-log-n-c-java-python


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        m = r = 1
        while n > 0:
            ones += (n + 8) / 10 * m + (n % 10 == 1) * r
            r += n % 10 *m
            m *= 10
            n /= 10
        return ones

if __name__ == '__main__':
    sol = Solution()
    print sol.countDigitOne(13)
