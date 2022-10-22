# Ref: https://leetcode.com/problems/maximum-number-of-accepted-invitations/discuss/1148032/Python-A-very-simple-Hungarian-implementation

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        match = [-1] * n
        seen = [False] * n

        def dfs(boy):
            for girl in range(n):
                if grid[boy][girl] and not seen[girl]:
                    seen[girl] = True
                    if match[girl] == -1 or dfs(match[girl]):
                        match[girl] = boy
                        return True
            return False

        ans = 0
        for i in range(m):
            seen = [False] * n
            if dfs(i):
                ans += 1
        return ans
