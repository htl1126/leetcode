# Ref: https://leetcode.com/problems/candy-crush/discuss/109220/155-ms-Python-with-detailed-explanation-beat-100

class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        board = map(list, zip(*reversed(board)))
        m, n = len(board), len(board[0])

        while True:
            candy = set()
            for i in xrange(m):
                for j in xrange(2, n):
                    if board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        candy |= {(i, j), (i, j - 1), (i, j - 2)}
            for i in xrange(2, m):
                for j in xrange(n):
                    if board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        candy |= {(i, j), (i - 1, j), (i - 2, j)}
            if not candy:
                break
            for i, j in candy:
                board[i][j] = 0
            for i in xrange(m):
                row = filter(None, board[i])
                board[i] = row + [0 for _ in xrange(n - len(row))]
        board = list(reversed(map(list, zip(*board))))
        return board

if __name__ == "__main__":
    sol = Solution()
    print sol.candyCrush([[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714],[810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]])
