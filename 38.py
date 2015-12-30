# use itertools.groupby() consice solution but too slow
# source: https://leetcode.com/discuss/75204/4-5-lines-python-solutions

import sys
import itertools

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in xrange(n - 1):
            s = ''.join('{0}{1}'.format(len(list(group)), digit) for digit, group
                        in itertools.groupby(s))
        return s

if __name__ == '__main__':
    sol = Solution()
    print sol.countAndSay(int(sys.argv[1]))
