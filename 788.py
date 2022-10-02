# Ref: https://leetcode.com/problems/rotated-digits/discuss/116530/JavaPython-O(logN)-Time-O(1)-Space

class Solution:
    def rotatedDigits(self, n: int) -> int:
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        ans = 0
        digits = list(map(int, str(n)))
        for i, v in enumerate(digits):
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    ans += 7 ** (len(digits) - i - 1)
                if s.issubset(s1) and j in s1:
                    ans -= 3 ** (len(digits) - i - 1)
            if v not in s2:
                return ans
            s.add(v)
        return ans + (s.issubset(s2) and not s.issubset(s1))
