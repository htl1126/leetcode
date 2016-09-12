# ref: https://discuss.leetcode.com/topic/58426/another-python-solution


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total, size = sum(A), len(A)
        gmax = lmax = sum(i * A[i] for i in xrange(size))
        for i in xrange(size - 1, 0, -1):
            lmax += (total - A[i] * size)
            gmax = max(gmax, lmax)
        return gmax

if __name__ == '__main__':
    sol = Solution()
    print sol.maxRotateFunction([4, 3, 2, 6])
