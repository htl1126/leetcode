# Ref: https://leetcode.com/problems/backspace-string-compare/discuss/135603/JavaC%2B%2BPython-O(N)-time-and-O(1)-space

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                if S[i] == '#':
                    backS += 1
                else:
                    backS -= 1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                if T[j] == '#':
                    backT += 1
                else:
                    backT -= 1
                j -= 1
            if i >= 0 and j >=0 and S[i] == T[j]:
                i -= 1
                j -= 1
            else:
                break
        return i == j == -1
