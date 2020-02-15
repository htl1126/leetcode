# Ref: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/427981/python-stack
# Algo: stack

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack += [cur]
                cur = ''
            elif c == ')':
                if stack:
                    cur = stack.pop() + '(' + cur + ')'
            else:
                cur += c
        while stack:
            cur = stack.pop() + cur
        return cur

if __name__ == "__main__":
    sol = Solution()
    print sol.minRemoveToMakeValid("lee(t(c)o)de)")
