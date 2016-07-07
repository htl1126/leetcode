# ref: https://discuss.leetcode.com/topic/49771/java-simple-easy-understand
#              -solution-with-explanation


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        if b == 0:
            return a
        while b != 0:
            carry = a & b
            a ^= b
            b = carry << 1
        return a

if __name__ == '__main__':
    sol = Solution()
    print sol.getSum(3, 4)
