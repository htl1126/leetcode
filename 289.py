# ref: https://discuss.leetcode.com/topic/29054/easiest-java-
#              solution-with-explanation/2


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def get_neighbor_lives(board, row, col, i, j):
            pos_diffs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1],
                         [1, 0], [1, 1]]
            lives = 0
            for pos_diff in pos_diffs:
                x_diff, y_diff = pos_diff
                if 0 <= i + x_diff < row and 0 <= j + y_diff < col:
                    lives += board[i + x_diff][j + y_diff] & 1
            return lives

        if board == [[]]:
            return
        row, col = len(board), len(board[0])
        for i in xrange(row):
            for j in xrange(col):
                lives = get_neighbor_lives(board, row, col, i, j)
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        for i in xrange(row):
            for j in xrange(col):
                board[i][j] >>= 1
        return

if __name__ == '__main__':
    sol = Solution()
    board = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    sol.gameOfLife(board)
    print board
