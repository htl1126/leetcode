# ref: https://leetcode.com/discuss/97924/o-1-one-line-solution-without-loops


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (
            (num & (num - 1) == 0) and ((num & 0x55555555) == num))

if __name__ == '__main__':
    sol = Solution()
    print sol.isPowerOfFour(5)
