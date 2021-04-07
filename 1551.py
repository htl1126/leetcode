# Ref: https://leetcode.com/problems/minimum-operations-to-make-array-equal/discuss/1145077/Python-Math-oneliner-explained

class Solution:
    def minOperations(self, n: int) -> int:
        return n * n // 4
