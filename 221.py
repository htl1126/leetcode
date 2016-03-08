# source: https://leetcode.com/discuss/41736/share-my-concise-python-solution

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row_size = len(matrix)
        col_size = len(matrix[0])
        table = [[int(c) for c in matrix[i]] for i in xrange(len(matrix))]
        for i in xrange(1, row_size):
            for j in xrange(1, col_size):
                if matrix[i][j] == '1':
                    table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1
                else:
                    table[i][j] = 0
        return max([max(row) for row in table]) ** 2


if __name__ == '__main__':
    matrix = ['10100', '10111', '11111', '10010']
    sol = Solution()
    print sol.maximalSquare(matrix)
