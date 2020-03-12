# Ref: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/243819/Python-with-sort

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 1:
            return 0
        points.sort()
        ans, end = 1, points[0][1]
        for x, y in points[1:]:
            if x <= end:
                end = min(end, y)
            else:
                ans += 1
                end = y
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]])
