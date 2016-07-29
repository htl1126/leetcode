# ref: https://discuss.leetcode.com/topic/9350/python-dp-solution


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        table = [True] + [False for _ in xrange(length)]
        for i in p:
            if i != '*':
                for n in xrange(length - 1, -1, -1):
                    table[n + 1] = table[n] and (i == s[n] or i == '?')
            else:
                for n in xrange(1, length + 1):
                    table[n] = table[n] or table[n - 1]
            table[0] = table[0] and i == '*'
        return table[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch('aa', 'a*')
