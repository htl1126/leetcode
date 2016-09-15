# ref: https://discuss.leetcode.com/topic/42985/hint-for-the-pattern
# for n > 3, break n into 3's and 2's. 3's are as many as possible.


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
