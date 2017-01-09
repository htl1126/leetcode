# ref: https://discuss.leetcode.com/topic/66065/python-dfs-bests-85-tips-for-all-dfs
#              -in-matrix-question


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix
        m, n, ans = len(matrix), len(matrix[0]), []
        res = [[0] * n for _ in xrange(m)]

        def search(i, j, mask):
            res[i][j] |= mask
            for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                if 0 <= x < m and 0 <= y < n and res[x][y] & mask == 0 \
                   and matrix[i][j] <= matrix[x][y]:
                    search(x, y, mask)
        for i in xrange(m):
            search(i, 0, 1)
            search(i, n - 1, 2)
        for i in xrange(n):
            search(0, i, 1)
            search(m - 1, i, 2)
        for i in xrange(m):
            for j in xrange(n):
                if res[i][j] == 3:
                    ans.append([i, j])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.pacificAtlantic([[1, 2, 2, 3, 5],
                               [3, 2, 3, 4, 4],
                               [2, 4, 5, 3, 1],
                               [6, 7, 1, 4, 5],
                               [5, 1, 1, 2, 4]])
