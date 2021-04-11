# ref: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if not d[i][j]:
                val = matrix[i][j]
                d[i][j] = 1 + max(dfs(i - 1, j) if i - 1 >= 0 and val < matrix[i - 1][j] else 0,
                                  dfs(i, j - 1) if j - 1 >= 0 and val < matrix[i][j - 1] else 0,
                                  dfs(i, j + 1) if j + 1 < c and val < matrix[i][j + 1] else 0,
                                  dfs(i + 1, j) if i + 1 < r and val < matrix[i + 1][j] else 0)
            return d[i][j]
        if not matrix or not matrix[0]:
            return 0
        r, c = len(matrix), len(matrix[0])
        d = [[0] * c for _ in range(r)]
        return max(dfs(i, j) for i in range(r) for j in range(c))

if __name__ == '__main__':
    sol = Solution()
    print sol.longestIncreasingPath([[9, 9, 4],
                                     [6, 6, 8],
                                     [2, 1, 1]])
