# Ref: https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441306/JavaC%2B%2BPython-DP-solution
# Algo: dynamic programming

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        return sum(map(sum, matrix))

if __name__ == "__main__":
    sol = Solution()
    print sol.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]])
