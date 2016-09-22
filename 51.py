class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        sol = []

        def get_sol(q_pos, na, depth):
            if depth == n:
                sol.append([''.join('Q' if (i, j) in q_pos else '.'
                                    for j in xrange(n)) for i in xrange(n)])
            else:
                for j in xrange(n):
                    if (depth, j) not in na:
                        get_sol(q_pos | {(depth, j)}, na |
                                {(x, j) for x in xrange(n)} |
                                {(depth, x) for x in xrange(n)} |
                                {(x, depth + j - x) for x in xrange(n)
                                 if 0 <= x < n and 0 <= depth + j - x < n} |
                                {(x, x - (depth - j)) for x in xrange(n)
                                 if 0 <= x < n and 0 <= x - (depth - j) < n},
                                depth + 1)
        get_sol(set(), set(), 0)
        return sol

if __name__ == '__main__':
    sol = Solution()
    print sol.solveNQueens(4)
