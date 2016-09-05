# ref: https://discuss.leetcode.com/topic/18706/9-lines-python-148-ms


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        m, n = len(board), len(board[0])
        save = [ij for k in xrange(m + n) for ij in ((0, k), (m - 1, k), (k, 0),
                                                     (k, n - 1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]

if __name__ == '__main__':
    sol = Solution()
    board = [list('XXXX'), list('XOOX'), list('XXOX'), list('XOXX')]
    sol.solve(board)
    for row in board:
        print row
