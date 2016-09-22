# ref: https://discuss.leetcode.com/topic/20217/fast-short-and-easy-to
#              -understand-python-solution-11-lines-76ms


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        sol = []

        def get_sol(q_pos, xy_sum, xy_dif, depth):
            if depth == n:
                sol.append(['.' * q_pos[i] + 'Q' + '.' * (n - q_pos[i] - 1)
                            for i in xrange(n)])
            else:
                for j in xrange(n):
                    if j not in q_pos and depth + j not in xy_sum and \
                            depth - j not in xy_dif:
                        get_sol(q_pos + [j], xy_sum | {depth + j}, xy_dif |
                                {depth - j}, depth + 1)
        get_sol([], set(), set(), 0)
        return sol

if __name__ == '__main__':
    sol = Solution()
    print sol.solveNQueens(4)
