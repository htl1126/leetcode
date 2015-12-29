# O(lgn) division, source:https://leetcode.com/discuss/64576/ac-python-solution (faster)
#                         https://leetcode.com/discuss/52578/
#                                 python-o-lgn-solution-without-using-nested-while-loop

import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_int = 2147483647
        if dividend == 0:
            return 0
        if divisor == 0:
            return max_int
        is_negative = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        t = divisor
        q = 1
        while dividend >= t:
            t <<= 1
            q <<= 1
        while t >= divisor:
            if dividend >= t:
                dividend -= t
                ans += q
            t >>= 1
            q >>= 1
        ans = -ans if is_negative else ans
        return min(ans, max_int)

if __name__ == '__main__':
    sol = Solution()
    print sol.divide(int(sys.argv[1]), int(sys.argv[2]))
