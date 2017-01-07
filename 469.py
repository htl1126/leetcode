# ref: https://discuss.leetcode.com/topic/71543/python-o-n-by
#              -checking-the-directions-of-every-edge-learned
#              -from-robert-sedgewick-s-algorithm-course


class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def direction(a, b, c):
            return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

        last = None
        for i in xrange(1, len(points)):
            curr = direction(points[i - 2], points[i - 1], points[i])
            if curr == 0:
                continue
            if not last:
                last = curr
            else:
                if curr * last < 0:
                    return False
        if direction(points[-2], points[-1], points[0]) * last < 0:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isConvex([[0, 0], [0, 1], [1, 1], [1, 0]])
