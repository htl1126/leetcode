# ref: https://discuss.leetcode.com/topic/22684/fast-and-concise-
#              python-solution-using-dictionary


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        head, remainder = divmod(abs(numerator), abs(denominator))
        tail, seen = '', {}
        while remainder != 0:
            if remainder in seen:
                tail = tail[:seen[remainder]] + '(' +\
                    tail[seen[remainder]:] + ')'
                break
            seen[remainder] = len(tail)
            digit, remainder = divmod(remainder * 10, abs(denominator))
            tail = '{0}{1}'.format(tail, digit)
        return '{0}{1}{2}'.format(sign, head, (tail and '.' + tail))

if __name__ == '__main__':
    sol = Solution()
    print sol.fractionToDecimal(2, 9)
