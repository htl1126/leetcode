# Ref: https://leetcode.com/problems/toeplitz-matrix/discuss/113385/Python-Easy-and-Concise-Solution

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in xrange(len(matrix) - 1):
            for j in xrange(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.isToeplitzMatrix([
    [1,2],
  [2,2]
])
