# Ref: https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/discuss/260847/JavaC%2B%2BPython-O(S)

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if n > len(s) * 2:
            return False
        # for all i in binary form could be found in s,
        # i // 2 (or i >> 1) could be also found in s
        return all(bin(n)[2:] in s for n in range(n, n // 2, -1))
