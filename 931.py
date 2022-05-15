class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                t, v = float('inf'), matrix[i][j]
                for J in (j - 1, j, j + 1):
                    if 0 <= J < len(matrix):
                        t = min(t, v + matrix[i - 1][J])
                matrix[i][j] = t
        return min(matrix[-1])
