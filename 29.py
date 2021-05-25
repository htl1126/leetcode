# O(lgn) division, source:https://leetcode.com/discuss/64576/ac-python-solution (faster)
#                         https://leetcode.com/discuss/52578/
#                                 python-o-lgn-solution-without-using-nested-while-loop

import sys

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        is_neg = dividend * divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        ans, t, q = 0, divisor, 1
        while t <= dividend:
            t <<= 1
            q <<= 1
        while t >= divisor:
            if dividend >= t:
                dividend -= t
                ans += q
            t >>= 1
            q >>= 1
        ans = -ans if is_neg else ans
        return min(2 ** 31 - 1, max(ans, -2 ** 31))

if __name__ == '__main__':
    sol = Solution()
    print sol.divide(int(sys.argv[1]), int(sys.argv[2]))
