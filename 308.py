# ref: https://discuss.leetcode.com/topic/42522/python-94-5-simple-sum-
#              array-on-one-dimension-o-n-for-both-update-and-sumy


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for i in xrange(1, len(row)):
                row[i] += row[i - 1]
        self.matrix = matrix

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col - 1]
        diff = val - original
        for i in xrange(col, len(self.matrix[0])):
            self.matrix[row][i] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in xrange(row1, row2 + 1):
            if col1 == 0:
                ans += self.matrix[i][col2]
            else:
                ans += self.matrix[i][col2] - self.matrix[i][col1 - 1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)

if __name__ == '__main__':
    numMatrix = NumMatrix([[3, 0, 1, 4, 2],
                           [5, 6, 3, 2, 1],
                           [1, 2, 0, 1, 5],
                           [4, 1, 0, 1, 7],
                           [1, 0, 3, 0, 5]])
    print numMatrix.sumRegion(0, 1, 2, 3)
    numMatrix.update(1, 1, 10)
    print numMatrix.sumRegion(1, 2, 3, 4)
