# Ref: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/discuss/547229/Python-Union-Find

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        uf = {(i, j): (i, j) for i in xrange(-1, 2 * m) for j in xrange(-1, 2 * n)}

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def merge(i, j, di, dj):
            uf[find((i, j))] = find((i + di, j + dj))

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] in [2, 5, 6]:
                    merge(i * 2, j * 2, -1, 0)
                if grid[i][j] in [1, 3, 5]:
                    merge(i * 2, j * 2, 0, -1)
                if grid[i][j] in [2, 3, 4]:
                    merge(i * 2, j * 2, 1, 0)
                if grid[i][j] in [1, 4, 6]:
                    merge(i * 2, j * 2, 0, 1)
        return find((0, 0)) == find((2 * m - 2, 2 * n - 2))

if __name__ == "__main__":
    sol = Solution()
    print sol.hasValidPath()
