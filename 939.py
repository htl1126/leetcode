# Ref: https://leetcode.com/problems/minimum-area-rectangle/discuss/192021/Python-O(N1.5)-80ms

import collections

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        # impossible for points with different x/y values to form a rectangle
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        # accessing arrays is more expensive than dicts
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        ans = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in xrange(len(p[x])):
                for j in xrange(i):
                    y1, y2 = p[x][i], p[x][j]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * abs(y1 - y2))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0

if __name__ == "__main__":
    sol = Solution()
    print sol.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])
