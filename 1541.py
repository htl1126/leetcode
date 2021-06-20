# Ref: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/discuss/780366/C%2B%2B-O(n)-oror-Proper-explaination-oror-Without-Stack

class Solution:
    def minInsertions(self, s: str) -> int:
        # added: actually added right parentheses
        # right_need: additionally needed right parentheses
        added = right_need = 0
        for c in s:
            if c == '(':
                right_need += 2
                if right_need % 2:
                    added += 1
                    right_need -= 1
            elif c == ')':
                if right_need == 0:
                    added += 1
                    right_need += 1
                else:
                    right_need -= 1
        return added + right_need
