# ref: https://leetcode.com/discuss/52945/python-68-ms-code


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        ans = 0
        num_pts = len(points)
        for i in xrange(num_pts):
            same = 0
            dic = {'i': 1}
            for j in xrange(i + 1, num_pts):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                    continue
                if tx == points[i].x:
                    slope = 'i'
                else:
                    slope = float(ty - points[i].y) / (tx - points[i].x)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            ans = max(ans, max(dic.values()) + same)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.maxPoints([Point(0, 0), Point(1, 0)])
