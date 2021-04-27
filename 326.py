# Ref: https://leetcode.com/problems/power-of-three/discuss/77977/Math-1-liner-no-log-with-explanation

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 == 3 ** 19 % n
