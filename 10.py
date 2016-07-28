class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        table = [[False for _ in xrange(m + 1)] for _ in xrange(n + 1)]
        table[0][0] = True
        for i in xrange(1, n + 1):
            x = p[i - 1]
            if x == '*' and i > 1:
                table[i][0] = table[i - 2][0]
            for j in xrange(1, m + 1):
                if x == '*':
                    table[i][j] = table[i - 2][j] or table[i - 1][j] or (
                        table[i - 1][j - 1] and p[i - 2] == s[j - 1]) or (
                        table[i][j - 1] and p[i - 2] == '.')
                elif x == '.' or x == s[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
        return table[n][m]

if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch('aab', 'c*a*b')
