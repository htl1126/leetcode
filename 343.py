# ref: https://discuss.leetcode.com/topic/42985/hint-for-the-pattern


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return [1, 1, 2][n - 1]
        if n % 3 == 0:
            return 3 ** (n / 3)
        return 3 ** (n / 3 - (2 - n % 3)) * 2 ** (3 - n % 3)

if __name__ == '__main__':
    sol = Solution()
    print sol.integerBreak(14)
