class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        box, row, col = (dict((i, set()) for i in range(1, 10)),
                         dict((i, set()) for i in range(1, 10)), 
                         dict((i, set()) for i in range(1, 10)))
        empty = []
        found = [False]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[int(board[i][j])].add(i)
                    col[int(board[i][j])].add(j)
                    box[int(board[i][j])].add((i // 3) * 3 + j // 3)
                else:
                    empty.append((i, j))
        n = len(empty)
        def solve(step, cur_ans):
            if step == n:
                for idx, (i, j) in enumerate(empty):
                    board[i][j] = str(cur_ans[idx])
                found[0] = True
            else:
                i, j = empty[step]
                for v in range(1, 10):
                    if i not in row[v] and j not in col[v] and (i // 3) * 3 + j // 3 not in box[v] and not found[0]:
                        row[v].add(i)
                        col[v].add(j)
                        box[v].add((i // 3) * 3 + j // 3)
                        solve(step + 1, cur_ans + [v])
                        row[v].discard(i)
                        col[v].discard(j)
                        box[v].discard((i // 3) * 3 + j // 3)
        solve(0, [])
        return
