# ref: https://discuss.leetcode.com/topic/51356/two-python-solutions
# ref: https://discuss.leetcode.com/topic/51358/java-dp-solution


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        need = [[0] * (n + 1) for _ in xrange(n + 1)]
        for lo in xrange(n, 0, -1):
            for hi in xrange(lo + 1, n + 1):
                need[lo][hi] = min(k + max(need[lo][k - 1], need[k + 1][hi])
                                   for k in xrange(lo, hi))
        return need[1][n]

if __name__ == '__main__':
    sol = Solution()
    print sol.getMoneyAmount(3)
