# Ref: https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/discuss/1486326/Python3-row-by-row-and-col-by-col

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        w_lst = [word, word[::-1]]
        for x in board, zip(*board):
            for row in x:
                for s in "".join(row).split('#'):
                    for w in w_lst:
                        if len(s) == len(w) and all(s_c in (' ', w_c) for s_c, w_c in zip(s, w)):
                            return True
        return False
