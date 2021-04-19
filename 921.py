# Ref: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/181132/C%2B%2BJavaPython-Straight-Forward-One-Pass

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = right = 0
        for c in S:
            """ This part is easier to understand but slower
            if c == '(':
                right += 1
            elif right > 0:
                right -= 1
            else:
                left += 1
            """
            if c == ')' and right == 0:
                left += 1
            else:
                right += 1 if c == '(' else -1
        return left + right
