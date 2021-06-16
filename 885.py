# Ref: https://leetcode.com/problems/spiral-matrix-iii/discuss/158970/C%2B%2BJavaPython-112233-Steps

class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        dx, dy, n = 0, 1, 0
        while len(res) < R * C:
            for i in range(n // 2 + 1):
                if 0 <= r0 < R and 0 <= c0 < C:
                    res.append([r0, c0])
                r0, c0 = r0 + dx, c0 + dy
            dx, dy, n = dy, -dx, n + 1  # could be derived with the rotation matrix where theta = -pi / 2
        return res
