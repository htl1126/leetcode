class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0

        def get_sol(q_pos, xy_sum, xy_dif, depth):
            if depth == n:
                self.ans += 1
            else:
                for j in xrange(n):
                    if j not in q_pos and depth + j not in xy_sum and \
                            depth - j not in xy_dif:
                        get_sol(q_pos + [j], xy_sum | {depth + j}, xy_dif |
                                {depth - j}, depth + 1)
        get_sol([], set(), set(), 0)
        return self.ans
