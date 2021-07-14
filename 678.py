# Ref: https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis
# Ref: https://leetcode.com/problems/valid-parenthesis-string/discuss/543521/Java-Count-Open-Parenthesis-O(n)-time-O(1)-space-Picture-Explain
# Ref: https://leetcode.com/problems/valid-parenthesis-string/discuss/107577/Short-Java-O(n)-time-O(1)-space-one-pass

class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        # We keep an interval of ')' needed with [cmin, cmax]
        # So when cmin is less than 0, we 'eliminate' the 'route'
        for c in s:
            if c == '(':
                cmax += 1
                cmin += 1
            if c == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if c == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False  # early stop the process when the upperbound < 0
        return cmin == 0  # cmin == 0 means we can eliminate all the '('

if __name__ == "__main__":
    sol = Solution()
    print sol.checkValidString("(*))")
