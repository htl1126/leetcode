# Ref: https://leetcode.com/problems/knight-probability-in-chessboard/discuss/143583/Python-short-and-simple-DFS-w-memoization

class Solution:
    def knightProbability(self, n: int, K: int, row: int, column: int) -> float:
        memo = {}
        def find(i, j, p, k):
            if 0 <= i < n and 0 <= j < n:
                if k < K:
                    new_p = 0
                    for x, y in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
                        if (i + x, j + y, k) not in memo:
                            memo[(i + x, j + y, k)] = find(i + x, j + y, p / 8, k + 1)
                        new_p += memo[(i + x, j + y, k)]
                    return new_p
                else:
                    return p
            else:
                return 0
        return find(row, column, 1, 0)
