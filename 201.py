# ref: https://discuss.leetcode.com/topic/28538/java-python-easy-solution-with
#              -explanation


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i

if __name__ == '__main__':
    sol = Solution()
    print sol.rangeBitwiseAnd(5, 7)
