# Ref: https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/585632/JavaC%2B%2BPython-Easy-Prove

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ans, a, b = 0, 1, 1
        while b <= k:
            a, b = b, a + b
        while a > 0:
            if a <= k:
                k -= a
                ans += 1
            a, b = b - a, a
        return ans
