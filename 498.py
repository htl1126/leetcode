# Ref: https://leetcode.com/problems/diagonal-traverse/discuss/97767/Simply-Python-Solution

import collections

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        lines = collections.defaultdict(list)
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                lines[i + j].append(matrix[i][j])
        for k in xrange(len(lines)):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
