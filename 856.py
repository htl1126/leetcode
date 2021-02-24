# Ref: https://leetcode.com/problems/score-of-parentheses/discuss/141777/C%2B%2BJavaPython-O(1)-Space

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack, cur = [], 0
        for c in S:
            if c == '(':
                stack.append(cur)
                cur = 0
            else:
                cur = stack.pop() + cur + max(cur, 1)
        return cur
