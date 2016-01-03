# make use of dictionary, source: 
# https://leetcode.com/discuss/72452/python-solution-simple-and-fast

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        map_col = [{} for _ in xrange(9)]
        map_row = [{} for _ in xrange(9)]
        map_cell = [[{} for _ in xrange(3)] for __ in xrange(3)]
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    continue
                char = board[i][j]
                if char in map_col[j]:
                    return False
                else:
                    map_col[j][char] = [i, j]
                if char in map_row[i]:
                    return False
                else:
                    map_row[i][char] = [i, j]
                if char in map_cell[i / 3][j / 3]:
                    return False
                else:
                    map_cell[i / 3][j / 3][char] = [i, j]
        return True

if __name__ == '__main__':
    sol = Solution()
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    print sol.isValidSudoku(board)
