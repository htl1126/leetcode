# ref: https://discuss.leetcode.com/topic/46144/short-hack-in-python
import re


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        patterns = [['']]
        bad = ('[^2]*(13|31)|[^4]*(17|71)|[^6]*(39|93)|[^8]*(79|97)|'
               '[^5]*(19|28|37|46|64|73|82|91)')
        bad = re.compile(bad).match
        while len(patterns) <= n:
            patterns += [p + d for p in patterns[-1] for d in '123456789'
                         if d not in p and not bad(p + d)],  # note the ','
        return sum(map(len, patterns[m:n + 1]))

if __name__ == '__main__':
    sol = Solution()
    print sol.numberOfPatterns(1, 2)
