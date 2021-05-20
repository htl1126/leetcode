# Ref: https://leetcode.com/problems/cherry-pickup/discuss/109909/Python-cleanandcommented-O(N3)-DP

class Solution:
    def cherryPickup(self, grid) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[-1][-1] == -1:
            return 0
        
        memo = {}
        n = len(grid)
        
        def dp(i1, j1, i2, j2):
            if i1 > i2:
                return dp(i2, j2, i1, j1)
            if (i1, j1, i2, j2) not in memo:
                if any(i == n for i in (i1, j1, i2, j2)) or any(i == -1 for i in (grid[i1][j1], grid[i2][j2])):
                    return -1
                if i1 == j1 == i2 == j2 == n - 1:
                    return grid[-1][-1]
                max_sub_sol = max(dp(i1 + 1, j1, i2 + 1, j2), dp(i1 + 1, j1, i2, j2 + 1), dp(i1, j1 + 1, i2 + 1, j2), dp(i1, j1 + 1, i2, j2 + 1))
                ans = -1
                if max_sub_sol != -1:
                    if i1 == i2 and j1 == j2:
                        ans = max_sub_sol + grid[i1][j2]
                    else:
                        ans = max_sub_sol + grid[i1][j1] + grid[i2][j2]
                memo[i1, j1, i2, j2] = ans
            return memo[i1, j1, i2, j2]
        
        return max(dp(0, 0, 0, 0), 0)
