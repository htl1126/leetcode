# ref: https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/Python-3-DP-Explanation-with-pictures.
# ref: https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1345059/Python-DP-like-Solution

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        for i in range(m - 1):
            # analyze the code with case points = [[9, 2, 6], [1, 1, 1]]
            for j in range(n - 2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j + 1] - 1)
            for j in range(n):
                points[i][j] = max(points[i][j], points[i][j - 1] - 1 if j > 0 else 0)
                points[i + 1][j] += points[i][j]
        return max(points[-1])
