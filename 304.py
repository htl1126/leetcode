class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix == [] or matrix == [[]]:
            self.matrix = [[0, 0], [0, 0]]
            return
        matrix = [[0] * (len(matrix[0]) + 1)] + [[0] + row for row in matrix]
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j - 1]
            for j in xrange(1, len(matrix[0])):
                matrix[i][j] += matrix[i - 1][j]
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        m = self.matrix
        return m[row2][col2] - m[row1 - 1][col2] - m[row2][col1 - 1] + \
            m[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

if __name__ == '__main__':
    numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5],
                           [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print numMatrix.sumRegion(2, 1, 4, 3)
