# Ref: https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/440884/Python

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        def count((x, X), (y, Y)):
            if x > X or y > Y or not sea.hasShips(Point(X, Y), Point(x, y)):
                return 0
            if (x, y) == (X, Y):
                return 1
            xm = (x + X) / 2
            ym = (y + Y) / 2
            xRanges = (x, xm), (xm + 1, X)
            yRanges = (y, ym), (ym + 1, Y)
            return sum(count(xr, yr) for xr in xRanges for yr in yRanges)
        return count((bottomLeft.x, topRight.x), (bottomLeft.y, topRight.y))

