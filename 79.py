# ref: https://leetcode.com/discuss/54890/python-dfs-solution-with-comments


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
                word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        ans = self.dfs(board, i - 1, j, word[1:]) or \
            self.dfs(board, i, j - 1, word[1:]) or \
            self.dfs(board, i, j + 1, word[1:]) or \
            self.dfs(board, i + 1, j, word[1:])
        board[i][j] = tmp
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.exist([['A', 'B', 'C', 'E'],
                     ['S', 'F', 'C', 'S'],
                     ['A', 'D', 'E', 'E']], 'ABCCED')
