# ref: https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
# ref: https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF  # 2 ^ 31 - 1
        mask = 0xFFFFFFFF     # 2 ^ 32 - 1
        while b != 0:
            # "a ^ b" does the addition without carries
            # "a & b" gets the carries for each bit
            # "(a & b) << 1" moves carry bits one shift to the left.
            # They would be added for the next iteration
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, we have to flip all the leading zeros that are beyond 32-bit range to ones
        return a if a <= MAX_INT else ~(a ^ mask)

if __name__ == '__main__':
    sol = Solution()
    print sol.getSum(-1, 1)
