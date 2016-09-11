# ref: https://discuss.leetcode.com/topic/38068/another-python


class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.isSelfCrossing([2, 8, 10, 16, 4, 10, 7])
