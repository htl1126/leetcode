# Ref: https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = cmax = 0
        for c in s:
            if c == '(':
                cmin += 1
                cmax += 1
            if c == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if c == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0

if __name__ == "__main__":
    sol = Solution()
    print sol.checkValidString("(*))")
