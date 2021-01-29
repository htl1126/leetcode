# Ref: https://leetcode.com/problems/number-of-corner-rectangles/discuss/110200/Summary-of-three-solutions-based-on-three-different-ideas

class Solution:
    def countCornerRectangles(self, grid) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(0, m - 1):
            for j in range(i + 1, m):
                count = 0
                for k in range(n):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        count += 1
                ans += count * (count - 1) // 2
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.countCornerRectangles([[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]))
