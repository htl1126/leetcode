# ref: https://leetcode.com/discuss/58879/python-solution-with-explanation


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same, dif = k, k * (k - 1)
        for i in xrange(3, n + 1):
            same, dif = dif, same * (k - 1) + dif * (k - 1)
        return same + dif

if __name__ == '__main__':
    sol = Solution()
    print sol.numWays(3, 3)
