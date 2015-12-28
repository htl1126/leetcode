# DP solution, source: https://leetcode.com/discuss/66868/clean-python-dp-solution
#                      https://leetcode.com/discuss/43122/4-7-lines-python

import sys
from leetcode_util import read_list

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        table = []
        for i in xrange(n + 1):
            table.append([])
        table[0].append('')
        for i in xrange(n + 1):
            for j in xrange(i):
                table[i] += ['({0}){1}'.format(x, y) for x in table[j] for y in table[i - j - 1]]
        return table[n]

if __name__ == '__main__':
    sol = Solution()
    print sol.generateParenthesis(6)
