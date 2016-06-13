# ref: https://leetcode.com/discuss/20589/a-common-method-to-rotate-the-image


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        matrix.reverse()
        for i in xrange(size):
            for j in xrange(i + 1, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == '':
    sol = Solution()
