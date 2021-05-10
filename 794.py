class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # 0 <= n(X) - n(O) <= 1
        # "X" wins: n(X) = n(O) + 1
        # "O" wins: n(X) = n(O)
        # no wins : 0 <= n(X) - n(O) <= 1
        n_O = (board[0] + board[1] + board[2]).count("O")
        n_X = (board[0] + board[1] + board[2]).count("X")
        bd = list(map(list, board))
        # keep track of all lines and horizontal and vertical lines
        has_line = {"X": [False, False, False], "O": [False, False, False]}
        for piece in ["X", "O"]:
            if all(bd[i][i] == piece for i in range(3)):
                has_line[piece][0] = True
            if all(bd[i][2 - i] == piece for i in range(3)):
                has_line[piece][0] = True
            for i in range(3):
                if all(bd[i][j] == piece for j in range(3)):
                    if has_line[piece][1]:
                        return False
                    has_line[piece][0] = has_line[piece][1] = True
                if all(bd[j][i] == piece for j in range(3)):
                    if has_line[piece][2]:
                        return False
                    has_line[piece][0] = has_line[piece][2] = True
        return has_line["X"][0] == False and has_line["O"][0] == False and 0 <= n_X - n_O <= 1 or has_line["X"][0] == True and has_line["O"][0] == False and n_X == n_O + 1 or has_line["X"][0] == False and has_line["O"][0] == True and n_X == n_O
