# ref: https://discuss.leetcode.com/topic/59570/python-documented-solution-that
#              -is-easy-to-understand


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        d = {x: set() for x in stones}
        d[1].add(1)
        for x in stones[:-1]:
            for j in d[x]:
                for k in xrange(j - 1, j + 2):
                    if k > 0 and x + k in d:
                        d[x + k].add(k)
        return bool(d[stones[-1]])

if __name__ == '__main__':
    sol = Solution()
    print sol.canCross([0, 1, 3, 5, 6, 8, 12, 17])
