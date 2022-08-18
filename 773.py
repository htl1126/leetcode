# Ref: https://leetcode.com/problems/sliding-puzzle/discuss/113620/JavaPython-3-BFS-clean-codes-w-comment-Time-and-space%3A-O(m-*-n-*-(m-*-n)!).

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(n) for row in board for n in row)
        seen = {s}
        q = [(s, s.index('0'))]
        step, row, col = 0, len(board), len(board[0])
        while q:
            new_q = []
            for b, p in q:
                if b == "123450":
                    return step
                i, j = p // col, p % col
                for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                    if 0 <= x < row and 0 <= y < col:
                        t = [c for c in b]
                        t[p], t[x * col + y] = t[x * col + y], t[p]
                        s = ''.join(t)
                        if s not in seen:
                            seen.add(s)
                            new_q.append((s, x * col + y))
            q = new_q
            step += 1
        return -1
