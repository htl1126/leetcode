# Ref: https://leetcode.com/problems/leftmost-column-with-at-least-a-one/discuss/590135/Easy-Python-solution-O(M-%2B-N)

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        M, N = binaryMatrix.dimensions()
        r, c, ans = 0, N - 1, -1
        while r < M and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                ans = c
                c -= 1
            else:
                r += 1
        return ans
