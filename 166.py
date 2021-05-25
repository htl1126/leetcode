# ref: https://discuss.leetcode.com/topic/22684/fast-and-concise-
#              python-solution-using-dictionary


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        head, remainder = divmod(abs(numerator), abs(denominator))
        tail, seen = '', {}
        while remainder != 0:
            if remainder in seen:
                tail = tail[:seen[remainder]] + '(' + tail[seen[remainder]:] + ')'
                break
            seen[remainder] = len(tail)
            digit, remainder = divmod(remainder * 10, abs(denominator))
            tail += str(digit)
        return sign + str(head) + ('.' + tail if tail else '')

if __name__ == '__main__':
    sol = Solution()
    print sol.fractionToDecimal(2, 9)
