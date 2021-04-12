# Ref: https://leetcode.com/problems/making-a-large-island/discuss/127032/C%2B%2BJavaPython-Straight-Forward-O(N2)-with-Explanations

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # good example for calculating areas of connected regions
        def dfs(i, j, index):
            area = 0
            grid[i][j] = index
            for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    area += dfs(x, y, index)
            return area + 1
        
        areas = {0: 0}
        n = len(grid)
        index = 2
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[index] = dfs(i, j , index)
                    index += 1
                    
        ans = max(areas.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    t = 0
                    seen = set()
                    for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                        if 0 <= x < n and 0 <= y < n and grid[x][y] not in seen:
                            t += areas[grid[x][y]]
                            seen.add(grid[x][y])
                    ans = max(ans , t + 1)
        return ans
