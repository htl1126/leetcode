# Ref: https://leetcode.com/problems/battleships-in-a-board/discuss/90913/Share-my-7-line-code-1-line-core-code-3ms-super-easy

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] != 'X') and (j == 0 or board[i][j - 1] != 'X'):
                    ans += 1
        return ans
        
if __name__ == "__main__":
    sol = Solution()
    print sol.countBattleships()
