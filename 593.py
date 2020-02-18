# Ref: https://leetcode.com/problems/valid-square/discuss/103448/Simple-python-solution-by-comparing-distance
# Algo: math

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        dis = []
        dis.append((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        dis.append((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
        dis.append((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2)
        dis.append((p4[0] - p1[0]) ** 2 + (p4[1] - p1[1]) ** 2)
        dis.append((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
        dis.append((p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2)
        dis.sort()
        return 0 < dis[0] == dis[1] == dis[2] == dis[3] and 0 < dis[4] == dis[5] or 0 < dis[0] == dis[1] and 0 < dis[2] == dis[3] == dis[4] == dis[5]

if __name__ == "__main__":
    sol = Solution()
    print sol.validSquare([0, 0], [1, 1], [1, 0], [0, 1])
