# ref: https://discuss.leetcode.com/topic/28833/short-python-bfs


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while level:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in xrange(len(s))}

if __name__ == '__main__':
    sol = Solution()
    print sol.removeInvalidParentheses('()())()')
