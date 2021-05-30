# ref: https://discuss.leetcode.com/topic/30043/java-python-o-1-space-11-lines
#              -solution


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col, FirstRowHasZero = len(matrix), len(matrix[0]), not all(
            matrix[0])
        for i in xrange(1, row):
            for j in xrange(col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # visit j reversedly for this case
        # [[0,1,2,0],
        #  [3,4,5,2],
        #  [1,3,1,5]]
        for i in xrange(1, row):
            for j in xrange(col - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if FirstRowHasZero:
            matrix[0] = [0] * col

if __name__ == '__main__':
    sol = Solution()
    print sol.setZeroes([[1, 0, 1], [0, 1, 0]])
