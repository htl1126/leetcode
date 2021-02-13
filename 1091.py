class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        queue = collections.deque()
        if grid[0][0] == 0:
            queue.append([1, (0, 0)])
        r, c = len(grid), len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]
        while queue:
            length, (x, y) = queue.popleft()
            if (x, y) == (r - 1, c - 1):
                return length
            for dx, dy in d:
                if 0 <= x + dx < r and 0 <= y + dy < c and grid[x + dx][y + dy] == 0 and not visited[x + dx][y + dy]:
                    queue.append([length + 1, (x + dx, y + dy)])
                    visited[x + dx][y + dy] = True
        return -1
