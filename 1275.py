class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        move = collections.defaultdict(int)
        player = ["A", "B"]
        for m, (i, j) in enumerate(moves):
            for n, x in enumerate((i, j, i + j, i - j)):
                move[n, x, m % 2] += 1
                if move[n, x, m % 2] == 3:
                    return player[m % 2]
        return "Draw" if len(moves) == 9 else "Pending"
