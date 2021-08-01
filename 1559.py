# ref: https://leetcode.com/problems/detect-cycles-in-2d-grid/discuss/805691/Clean-Python-3-Union-and-Find

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def find(pos):
            if parents[pos] != pos:
                parents[pos] = find(parents[pos])
            return parents[pos]

        def union(pos1, pos2):
            parents[find(pos1)] = find(pos2)

        m, n = len(grid), len(grid[0])
        parents = {(i, j): (i, j) for i in range(m) for j in range(n)}
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                # When we find a shape like the following,
                #
                #          *
                #         **
                #
                # we can say we have found a cycle.
                if i > 0 and j > 0 and grid[i - 1][j] == grid[i][j - 1] == c and find((i - 1, j)) == find((i, j - 1)):
                    return True
                for x, y in (i - 1, j), (i, j - 1):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == c:
                        union((i, j), (x, y))
        return False
