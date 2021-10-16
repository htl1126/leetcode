class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_num = sum([len(s) - 2 for s in colors.split('B') if len(s) >= 3])
        b_num = sum([len(s) - 2 for s in colors.split('A') if len(s) >= 3])
        return a_num > b_num
