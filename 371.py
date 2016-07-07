# ref: https://discuss.leetcode.com/topic/49771/java-simple-easy-understand
#              -solution-with-explanation
# ref: https://discuss.leetcode.com/topic/49900/python-solution/2


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        mask = 0x100000000
        while b != 0:
            carry = a & b
            a = (a ^ b) % mask
            b = (carry << 1) % mask
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

if __name__ == '__main__':
    sol = Solution()
    print sol.getSum(-1, 1)
