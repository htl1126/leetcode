class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif char in dic:
                if not stack or stack[-1] != dic[char]:
                    return False
                stack.pop()
        return not stack

if __name__ == '__main__':
    sol = Solution()
    print sol.isValid('([)]')
