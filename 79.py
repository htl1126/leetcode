# ref: https://leetcode.com/discuss/54890/python-dfs-solution-with-comments


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def found(i, j, word):
            if not word:
                return True
            if 0 <= i < row and 0 <= j < col and board[i][j] == word[0]:
                c = board[i][j]
                board[i][j] = '#'
                ans = found(i + 1, j, word[1:]) or found(i - 1, j, word[1:]) \
                    or found(i, j - 1, word[1:]) or found(i, j + 1, word[1:])
                board[i][j] = c
                return ans
        if not board:
            return False
        row, col = len(board), len(board[0])
        for i in xrange(row):
            for j in xrange(col):
                if found(i, j, word):
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.exist([['A', 'B', 'C', 'E'],
                     ['S', 'F', 'C', 'S'],
                     ['A', 'D', 'E', 'E']], 'ABCCED')
