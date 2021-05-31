# Ref: https://leetcode.com/problems/valid-number/discuss/173977/Python-with-simple-explanation

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        seen_dot = seen_e = seen_digit = False
        for i, c in enumerate(s):
            if c in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif c == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif c in ['e', 'E']:
                if seen_e or not seen_digit:
                    return False
                seen_e, seen_digit = True, False
            elif c.isdigit():
                seen_digit = True
            else:
                return False
        return seen_digit
