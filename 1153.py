# Ref: https://leetcode.com/problems/string-transforms-into-another-string/discuss/355382/JavaC%2B%2BPython-Need-One-Unused-Character

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        m = {}
        for i, j in zip(str1, str2):
            if m.setdefault(i, j) != j:  # we can't convert one char to two different chars
                return False
        # there's no way to convert into a string having a thru z
        # MUST do for str2 not str1
        return len(set(str2)) < 26
