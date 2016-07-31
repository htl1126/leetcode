# ref: https://discuss.leetcode.com/topic/12840/one-line-python-solution-with
#              -comments


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [(i >> 1) ^ i for i in xrange(2 ** n)]

if __name__ == '__main__':
    sol = Solution()
    print sol.grayCode(3)
