# ref: https://discuss.leetcode.com/topic/9350/python-dp-solution

# Rewrite 44.py to be understood more easily. Actually it's a LCS variant

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        if len_p - p.count('*') > len_s:
            return False
        table = [[False for _ in xrange(len_s + 1)] for _ in xrange(len_p + 1)]
        table[0][0] = True
        if len(p) > 0:
            table[1][0] = table[0][0] and (p[0] == '*')
        for i in xrange(len_p):
            for j in xrange(len_s):
                if p[i] != '*':
                    table[i + 1][j + 1] = table[i][j] and (p[i] == s[j] or p[i] == '?')
                else:
                    table[i + 1][j + 1] = table[i][j + 1] or table[i + 1][j]
            if i < len(p) - 1:
                table[i + 2][0] = table[i + 1][0] and (p[i + 1] == '*')
        return table[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch('aa', 'a*')
