# Ref: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/451787/Python-O(m*n*k)-BFS-Solution-with-Explanation

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        if k >= m + n - 1:
            return m - 1 + n - 1
        visited = set((0, 0, k))
        q = [(0, 0, k, 0)]
        while q:
            new_q = []
            for i, j, k, step in q:
                for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 1 and k > 0 and (x, y, k - 1) not in visited:
                            visited.add((x, y, k - 1))
                            new_q.append((x, y, k - 1, step + 1))
                        if grid[x][y] == 0 and (x, y, k) not in visited:
                            if x == m - 1 and y == n - 1:
                                return step + 1
                            visited.add((x, y, k))
                            new_q.append((x, y, k, step + 1))
            q = new_q
        return -1
