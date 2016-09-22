class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        box, row, col = (dict((i, set()) for i in xrange(1, 10)),
                         dict((i, set()) for i in xrange(1, 10)),
                         dict((i, set()) for i in xrange(1, 10)))
        empty = []
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != '.':
                    row[int(board[i][j])].add(i)
                    col[int(board[i][j])].add(j)
                    box[int(board[i][j])].add((i / 3) * 3 + j / 3)
                else:
                    empty += (i, j),
        n = len(empty)

        def solve(step, cur_ans):
            if step == n:
                for idx, (i, j) in enumerate(empty):
                    board[i][j] = str(cur_ans[idx])
            else:
                i, j = empty[step]
                for v in xrange(1, 10):
                    if i not in row[v] and j not in col[v] and \
                            (i / 3) * 3 + j / 3 not in box[v]:
                        row[v].add(i)
                        col[v].add(j)
                        box[v].add((i / 3) * 3 + j / 3)
                        solve(step + 1, cur_ans + [v])
                        row[v].discard(i)
                        col[v].discard(j)
                        box[v].discard((i / 3) * 3 + j / 3)
        solve(0, [])
        return
