# Ref: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/discuss/780366/C%2B%2B-O(n)-oror-Proper-explaination-oror-Without-Stack

class Solution:
    def minInsertions(self, s: str) -> int:
        # added: the parentheses added in the middle of the input string
        # right_need: the parentheses appended to the end of the input string
        added = right_need = 0
        for c in s:
            if c == '(':
                right_need += 2      # we append two ")" when we see "("
                if right_need % 2:   # if we have odd number of ")" to be appended,
                    added += 1       # we have to move the lonely ")" in the middle
                    right_need -= 1  # and "right_needed" need to decreased by one
            elif c == ')':
                if right_need == 0:  # when we don't have ")" to be appended,
                    added += 1       # we put a "(" in the middle,
                    right_need += 1  # and need to append a ")" to the end
                else:
                    right_need -= 1
        return added + right_need
