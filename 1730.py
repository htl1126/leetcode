class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        q, visited = collections.deque(), set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append((i, j, 0))
                    visited.add((i, j))
                    break
            if q:
                break
        while q:
            i, j, step = q.popleft()
            for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    if grid[x][y] == '#':
                        return step + 1
                    if grid[x][y] == 'O':
                        visited.add((x, y))
                        q.append((x, y, step + 1))
        return -1
